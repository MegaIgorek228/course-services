"""Application configuration module."""

import functools
from typing import final

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Settings for the FastAPI application."""

    title: str = "Course service title"
    description: str = "Course service description"
    summary: str = "Course service summary"
    version: str = "0.1.0"


@final
class Settings(BaseSettings):
    """Main settings class."""

    app: AppSettings = Field(default_factory=AppSettings)

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )


@functools.lru_cache
def get_settings() -> Settings:
    """Returns the application settings."""
    return Settings()
