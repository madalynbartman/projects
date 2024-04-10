--match query
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
--match phrase query
GET 1/_search
{
    "query":{
        "match_phrase":{
            "headline":{
                "query": "Shape of you"
            }
        }
    }
}
--match phrase increases precision but reduces recall