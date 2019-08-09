from datetime import datetime
import uuid
from elasticsearch import Elasticsearch

es = Elasticsearch()

def add(doc):
    doc['timestamp'] = datetime.now()
    id = str(uuid.uuid4())
#    res = es.index(index="mymarket", doc_type='movements', id=1, body=doc)
    es.index(index="mymarket", doc_type='movements', id=id, body=doc)
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-refresh.html
    es.indices.refresh(index="mymarket")
#    print(res['result'])

def get(id):
    res = es.get(index="mymarket", doc_type='movements', id=id)
#    print(res['_source'])
    return res['_source']
    
def get_all():
    res = es.search(index="mymarket", body={"query": {"match_all": {}}})
#    print("Got %d Hits:" % res['hits']['total']['value'])
#    for hit in res['hits']['hits']:
#        print("%(timestamp)s %(productName)s: %(quantity)s" % hit["_source"])
    return res['hits']
    
def get_order(id):
    res = es.search(index="mymarket", body={"query": {"match": { "orderId": id }}})
    return res['hits']
