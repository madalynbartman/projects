/* first run a query, 
run aggregations on the query data, 
name these aggregations germany_average_unit_price,
then get the avg of all values of the field UnitPrice over all query documents,
this in turn will tell us the avg unit price of items sold in germany. */

-- this query clasue allows us to perform aggregations on a subset of documents
GET ecommerce_data/_search
{
    "size": 0,
    "query": {
        "match": {
            "Country": "Germany"}
        }
    },
    "eggs": {
        "germany_average_unit_price": {
            "avg": {
                "field": "UnitPrice"
            }
        }
    }
}

-- bucket aggregations allow you to aggregate on several subsets of documents

GET ecommerce_data/_search 
{
    "size": 0,
    "query": {
        "match": {
            "Country": "Germany"
        }
    },
    "aggs":{ 
        "germany_average_unit_price":{
            "avg": {
                "field": "UnitPrice"
            }
        }
    }
}

-- fixed interval = interval length is always constant
GET ecommerce_data/_search
{
    "size": 0, 
    "aggs": {
        "transactions_by_8_hrs": {
            "date_histogram": {
                "field": "InvoiceDate",
                "fixed_interval": "8h"
            }
        }
    }
}

-- calendar interval = interval may vary
-- monthly
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_by_month": {
      "date_histogram": {
        "field": "InvoiceDate",
        "calendar_interval": "1M"
      }
    }
  }
}

-- optional param - order = sort based in key values (in descending order in this ex)
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_by_month": {
      "date_histogram": {
        "field": "InvoiceDate",
        "calendar_interval": "1M",
        "order": {
          "_key": "desc"
        }
      }
    }
  }
}

-- increase my interval (increments of 10 in this ex)
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_per_price_interval": {
      "histogram": {
        "field": "UnitPrice",
        "interval": 10
      }
    }
  }
}

-- can add order below interval
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_per_price_interval": {
      "histogram": {
        "field": "UnitPrice",
        "interval": 10,
        "order": {
          "_key": "desc"
        }
      }
    }
  }
}

-- specify range
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_per_custom_price_ranges": {
      "range": {
        "field": "UnitPrice",
        "ranges": [
          {
            "to": 50
          },
          {
            "from": 50,
            "to": 200
          },
          {
            "from": 200
          }
        ]
      }
    }
  }
}

-- terms aggregations
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "top_5_customers": {
      "terms": {
        "field": "CustomerID",
        "size": 5
      }
    }
  }
}

-- terms aggregations sorted in ascending order
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "5_customers_with_lowest_number_of_transactions": {
      "terms": {
        "field": "CustomerID",
        "size": 5,
        "order": {
          "_count": "asc"
        }
      }
    }
  }
}


GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_per_day": {
      "date_histogram": {
        "field": "InvoiceDate",
        "calendar_interval": "day"
      },
      "aggs": {
        "daily_revenue": {
          "sum": {
            "script": {
              "source": "doc['UnitPrice'].value * doc['Quantity'].value"
            }
          }
        }
      }
    }
  }
}