import pytest
import rdflib


@pytest.fixture
def network_graph() -> rdflib.Graph:
    g = rdflib.Graph()
    return g.parse("demos/grasshopper/latest.ttl", format="turtle")
