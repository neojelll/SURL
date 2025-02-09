import strawberry
import uuid


@strawberry.type
class ShortenLink:
    short_link: str
    long_link: str
    expiration: int
    prefix: str


@strawberry.type
class ShortenLinkResponse:
    task_id: uuid.UUID
    short_link: str
    long_link: str
    expiration: int
    prefix: str


@strawberry.input
class ShortenLinkInput:
    long_link: str
    expiration: int
    prefix: str
