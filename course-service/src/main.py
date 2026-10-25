"""Main entry point for the course service application."""

import logging
import logging.config

import yaml

from core.config import get_settings
from web.app import create_app
from web.lifespans import lifespan_app
from web.routers import service_router

logger = logging.getLogger(__name__)

with open("log-config.yaml", encoding="utf-8") as f:
    log_config = yaml.safe_load(f)
    logging.config.dictConfig(log_config)

settings = get_settings()
routers = (service_router,)
app = create_app(settings, routers, lifespan=lifespan_app)
logger.debug(f"Created app = {app} with settings = {settings}")
