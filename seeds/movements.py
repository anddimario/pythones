import random
import uuid
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

es = Elasticsearch()

start = datetime.now()
end = start + timedelta(days=5)
buyer = ["rukawa", "sakuragi", "akagi", "mitsui", "miyagi"]
limit = 100

for _ in range(limit):
    random_date = start + (end - start) * random.random()
    id = str(uuid.uuid4())

    doc = {
        'orderId': random.randint(0, limit/2),
        'sku': random.randint(0, limit/2),
        'quantity': random.randint(0, limit/2),
        'price': random.randint(0, limit/2),
        'timestamp': random_date,
        'buyer': random.choice(buyer),
    }
    print(doc)
    es.index(index="mymarket", doc_type='movements', id=id, body=doc)

# for best buyer must enable buyer field as searchable to avoid error
# https://www.elastic.co/guide/en/elasticsearch/reference/current/fielddata.html
enable_field = {
  "properties": {
    "buyer": { 
      "type":     "text",
      "fielddata": "true"
    }
  }
}

es.indices.put_mapping(index="mymarket", body=enable_field)

# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-refresh.html
es.indices.refresh(index="mymarket")