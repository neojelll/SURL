import strawberry

@strawberry.type
class ShortenedLink:
    id: str
    long_link: str
    short_link: str
    created_at: str
    