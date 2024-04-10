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