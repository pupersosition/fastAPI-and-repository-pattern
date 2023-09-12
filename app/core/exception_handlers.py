from fastapi.requests import Request
from fastapi.responses import JSONResponse
from loguru import logger
from core.errors import CreateError, UpdateError, DeleteError, NotFoundError


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
