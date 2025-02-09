from src.app.repositories.broker_repository import BrokerConsumer, BrokerProducer
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
import os


load_dotenv()


redirect_router = APIRouter(tags=["Redirect"])


@redirect_router.get('/{short_link}')
async def redirect_to_link(short_link: str):
    async with BrokerProducer() as producer:
        await producer.send_message(os.environ['LINK_REDIRECT_TOPIC'], {'short_link': short_link})

    async with BrokerConsumer(os.environ['LINK_REDIRECT_REPLY_TOPIC'], os.environ['LINK_REDIRECT_GROUP_ID']) as consumer:
        payload: dict = await consumer.get_message()

    if payload['long_link']:
        return RedirectResponse(url=payload['long_link'], status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
