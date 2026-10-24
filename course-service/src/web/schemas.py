"""Pydantic schemas for the web layer."""

from pydantic import BaseModel, ConfigDict


class BaseSchemaModel(BaseModel):
    """Base schema with common configuration."""

    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, populate_by_name=True
    )


class ServiceInfo(BaseSchemaModel):
    """Schema for service health info."""

    healthy: bool = True