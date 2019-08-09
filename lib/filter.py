def select_type(type, id):
    term = {
        "term": {}
    }
    if type == "buyer":
        term["term"]["buyer"] = id
    if type == "sku":
        term["term"]["sku"] = id
    return term


def create(type, id, querystring):
    filter = {}
    if querystring is not None:
        filter = {
            "bool": {
                "must": []
            }
        }
        if "start_date" in querystring:
            filter["bool"]["must"].append({
                "range": {
                    "timestamp": {"gte": querystring["start_date"]}
                }
            })

        if "end_date" in querystring:
            filter["bool"]["must"].append({
                "range": {
                    "timestamp": {"lte": querystring["end_date"]}
                }
            })

        filter["bool"]["must"].append(select_type(type, id))
    else:
        filter = select_type(type, id)
    return filter
