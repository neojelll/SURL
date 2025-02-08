from dotenv import load_dotenv
import os
import strawberry
from api.repositories.broker_repository import BrokerConsumer, BrokerProducer
from .types import ShortenLinkResponse
from fastapi import HTTPException, status


load_dotenv()


@strawberry.type
class Query:
    @strawberry.field
    async def get_short_link(self, long_link: str) -> ShortenLinkResponse:
        async with BrokerProducer() as producer:
            await producer.send_message(os.environ['GET_LINK_TOPIC'], {'long_link': long_link})

        async with BrokerConsumer(os.environ['GET_LINK_REPLY_TOPIC'], os.environ['GET_LINK_GROUP_ID']) as consumer:
            payload: dict = await consumer.get_message()

        if not payload['short_link']:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

        return ShortenLinkResponse(**payload)
