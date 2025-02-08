import strawberry
from .types import ShortenLinkInput, ShortenLinkResponse
from api.repositories.broker_repository import BrokerProducer, BrokerConsumer
import uuid 
import os
from dotenv import load_dotenv


load_dotenv()


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
