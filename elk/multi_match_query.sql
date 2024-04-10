-- useful when you don't know the context of why the user is searching for something
-- ex seraching for michelle obama. Do they want publications by her or about her?
-- you can include results with her in author field as well as the headline and description field

--regular query
GET 1/_searchquery
{
    "query":{
        "multi_match": {
            "query": "Michelle Obama",
            "fields": [
                "headline",
                "short_description",
                "authors"
            ]
        }
    }
}
--boost the score of documents that have michelle obama in the headline
GET 1/_searchquery
{
    "query":{
        "multi_match": {
            "query": "Michelle Obama",
            "fields": [
                "headline^2",
                "short_description",
                "authors"
            ]
        }
    }
}

