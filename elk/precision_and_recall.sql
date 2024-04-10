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

GET news_headlines/_search
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