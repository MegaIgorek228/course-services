"""Lifespan event handlers."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan_service_router(_app: FastAPI):
    """Lifespan for the service router."""
    logger.debug("Lifespan (service router) startup")
    yield
    logger.debug("Lifespan (service router) shutdown")


@asynccontextmanager
async def lifespan_app(_app: FastAPI):
    """Lifespan for the main application."""
    logger.debug("Lifespan (app) startup")
    yield
    logger.debug("Lifespan (app) shutdown")
