"""Business logic services."""

from src.web.schemas import ServiceInfo


def get_service_info() -> ServiceInfo:
    """Returns basic service information."""
    return ServiceInfo()