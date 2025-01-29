from diagrams import Diagram
from diagrams.c4 import (
    Person,
    Relationship,
    System,
)


FILE_PATH = 'diagrams/system-context-diagram'
GRAPH_ATTR = {
    'splines': 'spline',
}


with Diagram(filename=FILE_PATH, show=False, direction='TB', graph_attr=GRAPH_ATTR):
    user = Person(
        name='SURL User',
        description='user who wants to shorten the URL',
    )

    surl = System(
        name='SURL',
        description='SURL is a service for fast and convenient shortening of long links into neat short links',
        external=False,
    )

    user >> Relationship('uses') << surl
