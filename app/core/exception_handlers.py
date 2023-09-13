from core.errors import CreateError, UpdateError, DeleteError, NotFoundError
from core.logging import logger
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded


async def create_error_handler(request: Request, exc: CreateError):
    logger.error(f"Failed to create resource: {exc.detail}")
    return JSONResponse(status_code=400, content={"detail": exc.detail})


async def update_error_handler(request: Request, exc: UpdateError):
    logger.error(f"Failed to update resource: {exc.detail}")
    return JSONResponse(status_code=400, content={"detail": exc.detail})


async def delete_error_handler(request: Request, exc: DeleteError):
    logger.error(f"Failed to delete resource: {exc.detail}")
    return JSONResponse(status_code=400, content={"detail": exc.detail})


async def not_found_error_handler(request: Request, exc: NotFoundError):
    logger.warning(f"Resource not found: {exc.detail}")
    return JSONResponse(status_code=404, content={"detail": exc.detail})


def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        content={"detail": "Too many requests"},
        status_code=429
    )
