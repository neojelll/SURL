from diagrams import Diagram
from diagrams.c4 import (
    Person,
    Container,
    Relationship,
    SystemBoundary,
    System,
    Database,
)


FILE_PATH = 'diagrams/container-diagram'
GRAPH_ATTR = {
    'splines': 'spline',
}


with Diagram(filename=FILE_PATH, show=False, direction='TB', graph_attr=GRAPH_ATTR):
    user = Person(
        name='SURL User',
        description='user who wants to shorten the URL',
    )

    with SystemBoundary('Containers'):
        telegram_bot = Container(
            name='Telegram Bot',
            description='Telegram bot for a user-friendly interface for using SURL',
        )

        api = Container(
            name='APIGateway',
            technology='FastAPI',
            description='Handles and routes [HTTP] requests\nRedirect URLs',
        )

        broker = Container(
            name='Message Queue',
            technology='Kafka',
            description='Handles event routing and delivery\nProcesses URL generation requests',
        )

        shortener_service = Container(
            name='Shortener Service',
            technology='Python',
            description='Shorten URLs',
        )

        database = Database(
            name='Databse',
            technology='PostgreSQL',
            description='Stores original and shortened URLs\nStores expiration',
        )

        cache = Container(
            name='Cache',
            technology='Redis',
            description='Stored frequently requested URLs',
        )

        expiration_manager = Container(
            name='Expiration Manager',
            technology='Python',
            description='Checks for expired URLs in URL Database\nRemoves them',
        )

    user >> Relationship('Uses SURL', style='bold') << telegram_bot >> Relationship('sending long URL') << api

    user >> Relationship('Uses SURL', style='bold') << api >> Relationship('sending long URL in topic and consume long URL for topic') << broker

    api >> Relationship('try to request long url from db cache') << database

    api >> Relationship('try to request long url from db cache') << cache

    broker >> Relationship('consume long URL for topic and send short URL in topic') << shortener_service

    shortener_service >> Relationship('create records with long URL, short URL, expiration') >> database << Relationship('deleted continue expirated URLs') << expiration_manager

    shortener_service >> Relationship('create records and checking the short URL for existence') << cache
