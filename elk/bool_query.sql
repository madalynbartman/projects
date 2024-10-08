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
-- should clauses
GET Enter_name_of_the_index_here/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "Enter match or match_phrase here: {
          "Enter the name of the field": "Enter the value you are looking for" 
         }
        },
       "should":[
         {
          "Enter match or match_phrase here": {
            "Enter the name of the field": "Enter the value you are looking for"
          }
        }
      ]
    }
  }

GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "headline": "Michelle Obama"
          }
        }
      ],
      "should": [
        {
          "match": {
            "headline": "Becoming"
          }
        },
        {
          "match": {
            "headline": "women"
          }
        },
        {
          "match": {
            "headline": "empower"
          }
        }
      ]
    }
  }
}

-- filter clauses 
GET Enter_name_of_the_index_here/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "Enter match or match_phrase here": {
          "Enter the name of the field": "Enter the value you are looking for" 
         }
        }
        ],
       "filter":{
          "range":{
             "date": {
               "gte": "Enter lowest value of the range here",
               "lte": "Enter highest value of the range here"
          }
        }
      }
    }
  }
}

GET news_headlines/_search
{
  "query": {
    "bool": {
      "must": [
        {
        "match_phrase": {
          "headline": "Michelle Obama"
          }
         }
        ],
       "filter":{
          "range":{
             "date": {
               "gte": "2014-03-25",
               "lte": "2016-03-25"
          }
        }
      }
    }
  }
}