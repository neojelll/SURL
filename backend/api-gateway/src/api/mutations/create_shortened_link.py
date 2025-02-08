import strawberry

from ..schemas.shortened_link import ShortenedLink

@strawberry.type
class Mutation:
    @strawberry.field
    async def create_shortened_link(long_link: str) -> ShortenedLink:
        async with 
