"""API routers."""

import logging

from fastapi import APIRouter

from src.core.services import get_service_info
from src.web.lifespans import lifespan_service_router
from src.web.schemas import ServiceInfo

logger = logging.getLogger(__name__)

service_router = APIRouter(
    prefix="/service", lifespan=lifespan_service_router, tags=["service"]
)


@service_router.get(
    path="",
    description="Service info route",
    response_model=ServiceInfo,
    status_code=200,
)
def info() -> ServiceInfo:
    """Returns service info."""
    return get_service_info()
