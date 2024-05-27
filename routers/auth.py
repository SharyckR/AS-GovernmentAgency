import os

import identity.web
import requests
from fastapi import Request, Depends, HTTPException, status, APIRouter
from fastapi.responses import RedirectResponse, JSONResponse

__version__ = "0.8.0"  # The version of this sample, for troubleshooting purpose

from routers import app_config

router = APIRouter(prefix='/auth', tags=['authentication'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


def get_auth(request: Request):
    auth = identity.web.Auth(
        session=request.session,
        client_id=app_config.CLIENT_ID,
        client_credential=app_config.CLIENT_SECRET,
    )
    return auth


@router.get("/login")
async def login(auth: identity.web.Auth = Depends(get_auth)):
    login_params = auth.log_in(scopes=app_config.SCOPE, redirect_uri=os.getenv('REDIRECT_URI'))
    return JSONResponse(content=login_params)


@router.get(app_config.REDIRECT_PATH)
async def auth_response(request: Request, auth: identity.web.Auth = Depends(get_auth)):
    result = auth.complete_log_in(dict(request.query_params))
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result["error"])
    return RedirectResponse(url=str(request.url_for("index")))


@router.get("/logout")
async def logout(request: Request, auth: identity.web.Auth = Depends(get_auth)):
    return RedirectResponse(url=str(auth.log_out(str(request.url_for("index")))))


@router.get("/")
async def index(request: Request, auth: identity.web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        return RedirectResponse(url=str(request.url_for("login")))
    return {"message": "Welcome!", "user": user, "version": __version__}


@router.get("/call_downstream_api")
async def call_downstream_api(auth: identity.web.Auth = Depends(get_auth)):
    token = auth.get_token_for_user(app_config.SCOPE)
    if "error" in token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    # Use access token to call downstream API
    response = requests.get(
        app_config.ENDPOINT,
        headers={'Authorization': f'Bearer {token["access_token"]}'},
        timeout=30,
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

