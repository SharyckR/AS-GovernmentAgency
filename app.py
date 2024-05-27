import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

from routers import (educational_agency_router, health_agency_router, legal_agency_router, person_router,
                     transport_agency_router, educational_history_router, health_history_router, case_history_router,
                     fine_history_router, vehicle_history_router, auth, send_email)
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
app = FastAPI(title='GOVERNMENT AGENCY')


app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv('SECRET')# Change this to a more secure key
)

origin = ['*']
app.add_middleware(CORSMiddleware,
                   allow_origins=origin,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])
app.include_router(send_email.router)
app.include_router(educational_agency_router.router)
app.include_router(health_agency_router.router)
app.include_router(legal_agency_router.router)
app.include_router(person_router.router)
app.include_router(transport_agency_router.router)
app.include_router(educational_history_router.router)
app.include_router(health_history_router.router)
app.include_router(case_history_router.router)
app.include_router(fine_history_router.router)
app.include_router(vehicle_history_router.router)
app.include_router(auth.router)


@app.get('/', tags=['app'])  # Tested
async def root(request: Request):
    try:
        if 'authorization' in dict(request.headers.items()):
            print(dict(request.headers.items())['authorization'])
    except KeyboardInterrupt as e:
        print(e)
    return {'Message': 'Welcome to our FastAPI'}
