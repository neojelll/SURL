from .db import DataBase
from .cache import Cache
import string
import random


async def generate_random_string(length=7):
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string


async def shortener(prefix):
    if prefix:
        random_string = await generate_random_string(4)
        short_url = f"http://localhost/{prefix}/{random_string}"
    random_string = await generate_random_string(7)
    short_url = f"http://localhost/{random_string}"
    return short_url


async def check_short_url(prefix=""):
    short_url = await shortener(prefix)
    async with Cache() as cache:
        if await cache.check_short_url(short_url):
            short_url = await shortener(prefix)
        else:
            async with DataBase() as db:
                if await db.check_short_url(short_url) is not None:
                    short_url = await shortener(prefix)
    return short_url
