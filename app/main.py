from fastapi import FastAPI
from routes import car, manufacturer
from routes import car

app = FastAPI()

app.include_router(car.router, tags=["Cars"], prefix="/cars")
app.include_router(manufacturer.router, tags=["Manufacturers"], prefix="/manufacturers")

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass
