from typing import List, Dict
from SPARQLWrapper import SPARQLWrapper, JSON

class WikiDataFetcher:
    def __init__(self, query: str):
        self.endpoint_url = "https://query.wikidata.org/sparql"
        self.sparql = SPARQLWrapper(self.endpoint_url)
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)

    def _json_to_dict(self, results: List[Dict]) -> List[Dict]:
        new_results = []
        for result in results:
            new_result = {}
            for key in result:
                new_result[key] = result[key]["value"]
            new_results.append(new_result)
        return new_results

    def load(self) -> List[Dict]:
        results = self.sparql.queryAndConvert()["results"]["bindings"]
        results = self._json_to_dict(results)
        return results


