-- the bool query has must and must not clauses
-- can also specify should and filter
-- should == nice to have
-- filter == would they fit into a yes or no category. ex: applicant is either in or not in the city with the job
-- all of these are optional

---match phrase query
GET 1/_search
{
    "query": {
        "match_phrase": {
            "headline": "Michelle Obama"
        }
    },
    "aggregations": {
        "category_mentions":{
            "terms": {
                "field": "category",
                "size": 100
            }
        }
    }
}
--- bool query with must clause
GET 1/_search
{
    "query": {
        "bool": {
            "must": [
                {
                "match_phrase": {
                    "headline": "Michelle Obama"
                }
                },
                {
                    "match": {
                        "category": "POLITICS"
                    }
                }
            ]
        }
    }
}
-- bool query with must & must not clause
GET 1/_search
{
    "query": {
        "bool": {
            "must": {
                "match_phrase": {
                    "headline": "Michelle Obama"
                  }
                },
                "must_not":[
                    {
                    "match": {
                        "category": "WEDDINGS"
                    }
                }
            ]
        }
    }
}