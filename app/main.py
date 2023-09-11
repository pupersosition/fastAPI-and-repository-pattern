from fastapi import FastAPI
from routes import car, manufacturer

app = FastAPI()

app.include_router(car.router, tags=["Cars"], prefix="/cars")
app.include_router(manufacturer.router, tags=["Manufacturers"], prefix="/manufacturers")

@app.on_event("startup")
async def startup():
    # Place any startup events you'd want to run here.
    pass

@app.on_event("shutdown")
async def shutdown():
    # Place any cleanup code here.
    pass
