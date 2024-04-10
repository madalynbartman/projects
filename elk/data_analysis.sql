GET 1/_search

GET 1/_search
{
    "track_total_hits": true
}

GET 1/_search
{
    "query": {
        "range": {
            "date": {
                "gte": "2015-06-20",
                "lte": "2015-09-22"
            }
        }
    }
}

GET 1/_search
{
    "aggs": {
        "by_category": {
            "terms": {
                "field": "category",
                "size": 100
            }
        }
    }
}