from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def fetch_security_events():
    query = {"size": 100, "query": {"match_all": {}}}
    res = es.search(index="gcp-audit", body=query)
    return [hit["_source"] for hit in res["hits"]["hits"]]
