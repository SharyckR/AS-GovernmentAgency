from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (educational_agency_router, health_agency_router, legal_agency_router, person_router,
                     transport_agency_router, educational_history_router, health_history_router, case_history_router,
                     fine_history_router, vehicle_history_router)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
async def root():
    return {'Message': 'Welcome to our FastAPI'}
