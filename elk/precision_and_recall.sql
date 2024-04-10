GET 1/_search 
{
    "query": {
        "match": {
            "headline": {
                "query": "Khloe Kardashian Kendall Jenner"
            }
        }
    }
}
-- the and operator strings together multiple search terms for better results
GET 1/_search
{
    "query": {
        "match": {
            "headline": {
                "query": "Khloe Kardashian Kendall Jenner",
                "operator": "and"
            }
        }
    }
}
-- for all the hits, at least 3 search terms need to be included in the headline
GET 1/_search
{
    "query": {
        "match": {
            "headline": {
                "query": "Khloe Kardashian Kendall Jenner",
                "minimum_should_match": 3
            }
        }
    }
}