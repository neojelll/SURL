import strawberry
from .types import ShortenLinkInput, ShortenLinkResponse
from src.app.repositories.broker_repository import BrokerProducer, BrokerConsumer
import uuid 
import os
from dotenv import load_dotenv
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

        if payload['short_link']:
            return ShortenLinkResponse(**payload)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")



@strawberry.type
class Mutation:
    @strawberry.mutation
    async def shorten_link(self, input: ShortenLinkInput) -> ShortenLinkResponse:
        payload = {
            "task_id": uuid.uuid4(),
            "long_link": input.long_link,
            "expiration": input.expiration,
            "prefix": input.prefix,
        }

        async with BrokerProducer() as producer:
            await producer.send_message(os.environ['CREATE_LINK_TOPIC'], payload)

        async with BrokerConsumer(os.environ['CREATE_LINK_REPLY_TOPIC'], os.environ['CREATE_LINK_GROUP_ID']) as consumer:
            short_link: str = await consumer.get_message()

        return ShortenLinkResponse(**payload, short_link=short_link)
