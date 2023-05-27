from appsilon.ext.assets.wiki_data_fetcher import WikiDataFetcher


class MockSPARQWrapper:
    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.query = None
        self.return_format = None

    def setQuery(self, query):
        self.query = query

    def setReturnFormat(self, return_format):
        self.return_format = return_format

    def queryAndCovert(self):
        return {"results": {"bindings": []}}


def test_wiki_data_fetcher(monkeypatch):
    monkeypatch.setattr("appsilon.ext.assets.wiki_data_fetcher.SPARQLWrapper", MockSPARQWrapper)

    query = "SELECT ?item WHERE { ?item wdt:P31 wd:Q146. }"
    fetcher = WikiDataFetcher(query)

    assert fetcher.endpoint_url == "https://query.wikidata.org/sparql"

    results = [
        {"key1": {"value": "value1"}, "key2": {"value": "value2"}},
        {"key1": {"value": "value3"}, "key2": {"value": "value4"}},
    ]
    expected_results = [
        {"key1": "value1", "key2": "value2"},
        {"key1": "value3", "key2": "value4"},
    ]
    assert fetcher._json_to_dict(results) == expected_results

    query_result = {
        "results": {
            "bindings": [
                {"key1": {"value": "value1"}, "key2": {"value": "value2"}},
                {"key1": {"value": "value3"}, "key2": {"value": "value4"}},
            ]
        }
    }
    fetcher.sparql.queryAndConvert = lambda: query_result
    assert fetcher.load() == expected_results
