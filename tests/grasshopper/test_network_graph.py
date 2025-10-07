import rdflib


def test_no_duplicate_bacnet_device_ids(network_graph: rdflib.Graph):

    ns1 = rdflib.Namespace("http://data.ashrae.org/bacnet/2020#")

    query = """
    SELECT ?deviceInstance (GROUP_CONCAT(?device; separator=", ") AS ?devices)
    WHERE {
    ?device a ns1:Device ;
            ns1:device-instance ?deviceInstance .
    }
    GROUP BY ?deviceInstance
    HAVING (COUNT(?device) > 1)
    """

    results = network_graph.query(query, initNs={"ns1": ns1})
    duplicates = list(results)
    assert duplicates == [], f"Duplicate BACnet device-instance IDs found: {duplicates}"

