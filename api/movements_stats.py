from elasticsearch import Elasticsearch
from lib import filter

es = Elasticsearch()


def total_price():
    body = {
        "size": 0,  # use this to avoid hits returned with aggs: https://www.elastic.co/guide/en/elasticsearch/reference/current/returning-only-agg-results.html
        "aggs": {
            "total": {"sum": {"field": "price"}}
        }
    }
    results = es.search(index="mymarket", body=body)
    return results['aggregations']['total']['value']

def total_quantity():
    body = {
        "size": 0,  # use this to avoid hits returned with aggs: https://www.elastic.co/guide/en/elasticsearch/reference/current/returning-only-agg-results.html
        "aggs": {
            "total": {"sum": {"field": "quantity"}}
        }
    }
    results = es.search(index="mymarket", body=body)
    return results['aggregations']['total']['value']

def total_order(id):
    body = {
        "size": 0,  # use this to avoid hits returned with aggs: https://www.elastic.co/guide/en/elasticsearch/reference/current/returning-only-agg-results.html
        "aggs": {
            "order": {
                "filter": {"term": {"orderId": id}},
                "aggs": {
                    "total": {"sum": {"field": "price"}}
                }
            }
        }
    }
    results = es.search(index="mymarket", body=body)
    return results['aggregations']['order']


def total_product(sku, querystring):
    filter_es = filter.create("sku", sku, querystring)
    body = {
        "size": 0,  # use this to avoid hits returned with aggs: https://www.elastic.co/guide/en/elasticsearch/reference/current/returning-only-agg-results.html
        "aggs": {
            "product": {
                "filter": filter_es,
                "aggs": {
                    "total": {"sum": {"field": "price"}}
                }
            }
        }
    }
    results = es.search(index="mymarket", body=body)
    return results['aggregations']['product']


def total_buyer(buyer, querystring):
    filter_es = filter.create("buyer", buyer, querystring)
    body = {
        "size": 0,  # use this to avoid hits returned with aggs: https://www.elastic.co/guide/en/elasticsearch/reference/current/returning-only-agg-results.html
        "aggs": {
            "buyer": {
                "filter": filter_es,
                "aggs": {
                    "total": {"sum": {"field": "price"}}
                }
            }
        }
    }
    results = es.search(index="mymarket", body=body)
    return results['aggregations']['buyer']


def best_buyers():
    body = {
        "size": 0,
        "aggs": {
            "best_buyers": {
                "terms": {
                    "field": "buyer",
                    "size": 5,  # elements in list
                    "order": {"sum_agg": "desc"}
                },
                "aggs": {
                    "sum_agg": {
                        "sum": {
                            "field": "price"
                        }
                    }
                }
            }
        }
    }
    results = es.search(index="mymarket", body=body)
    return results["aggregations"]["best_buyers"]["buckets"]


def best_products():
    body = {
        "size": 0,
        "aggs": {
            "best_products": {
                "terms": {
                    "field": "sku",
                    "size": 5,  # elements in list
                    "order": {"sum_agg": "desc"}
                },
                "aggs": {
                    "sum_agg": {
                        "sum": {
                            "field": "price"
                        }
                    }
                }
            }
        }
    }
    results = es.search(index="mymarket", body=body)
    return results["aggregations"]["best_products"]["buckets"]
