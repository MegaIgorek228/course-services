"""FastAPI application factory."""

from fastapi import FastAPI


def create_app(settings, routers: tuple, **kwargs) -> FastAPI:
    """Creates and configures the FastAPI application."""
    app_params = {**settings.app.model_dump(), **kwargs}
    app = FastAPI(**app_params)
    for router in routers:
        app.include_router(router)
    return app
