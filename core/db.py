from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .config import settings

import os

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
