GET 1/_search
{
    "query":{
        "match":{
            "headline":{
                "query": "Shape of you"
            }
        }
    }
}