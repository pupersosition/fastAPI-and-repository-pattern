from fastapi import FastAPI
from routes import car
from routes import manufacturer
from slowapi.errors import RateLimitExceeded

from core.errors import CreateError, UpdateError, DeleteError, NotFoundError
from core.exception_handlers import (create_error_handler, update_error_handler,
                                     delete_error_handler, not_found_error_handler, rate_limit_exceeded_handler)
from core.rate_limit import limiter

app = FastAPI()
app.state.limiter = limiter

app.include_router(car.router, tags=["Cars"], prefix="/cars")
app.include_router(manufacturer.router, tags=["Manufacturers"], prefix="/manufacturers")

app.add_exception_handler(CreateError, create_error_handler)
app.add_exception_handler(UpdateError, update_error_handler)
app.add_exception_handler(DeleteError, delete_error_handler)
app.add_exception_handler(NotFoundError, not_found_error_handler)
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass
