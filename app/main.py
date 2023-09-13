from fastapi import FastAPI
from routes import car
from routes import manufacturer

from core.errors import CreateError, UpdateError, DeleteError, NotFoundError
from core.exception_handlers import (create_error_handler, update_error_handler,
                                     delete_error_handler, not_found_error_handler)

app = FastAPI()

app.include_router(car.router, tags=["Cars"], prefix="/cars")
app.include_router(manufacturer.router, tags=["Manufacturers"], prefix="/manufacturers")

app.add_exception_handler(CreateError, create_error_handler)
app.add_exception_handler(UpdateError, update_error_handler)
app.add_exception_handler(DeleteError, delete_error_handler)
app.add_exception_handler(NotFoundError, not_found_error_handler)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
