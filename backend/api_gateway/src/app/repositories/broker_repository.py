from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from dotenv import load_dotenv
import os
import json


load_dotenv()


class BrokerProducer:
    def __init__(self) -> None:
        self.producer = AIOKafkaProducer(
            bootstrap_servers=os.environ['BROKER_URL'],
            value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8'),
        )

    async def __aenter__(self):
        await self.producer.start()
        return self
    

    async def send_message(self, topic: str, payload: dict):
        await self.producer.send_and_wait(topic, payload)


    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.producer.flush()
        await self.producer.stop()


class BrokerConsumer:
    def __init__(self, topic: str, group_id: str):
        self.consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=os.environ['BROKER_URL'],
            enable_auto_commit=False,
            group_id=group_id,
            auto_offset_reset='latest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            session_timeout_ms=60000,
            heartbeat_interval_ms=3000,
            max_poll_interval_ms=300000
            )

    async def __aenter__(self):
        await self.consumer.start()
        return self
    

    async def get_message(self):
        message = await self.consumer.getone()

        if message.value:
            short_link = message.value.decode('utf-8')
            await self.consumer.commit()  
            return short_link
        
        raise ValueError('No message found')
    
         
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.consumer.stop()
