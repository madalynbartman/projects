/* first run a query, 
run aggregations on the query data, 
name these aggregations germany_average_unit_price,
then get the avg of all values of the field UnitPrice over all query documents,
this in turn will tell us the avg unit price of items sold in germany. */

-- metrics aggregations
GET ecommerce_data/_search

GET ecommerce_data/_search
{
  "aggs": {
    "sum_unit_price": {
      "sum": {
        "field": "UnitPrice"
      }
    }
  }
}

-- metircs with a size parameter
-- sum
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "sum_unit_price": {
      "sum": {
        "field": "UnitPrice"
      }
    }
  }
}

-- min
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "lowest_unit_price": {
      "min": {
        "field": "UnitPrice"
      }
    }
  }
}

-- max
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "highest_unit_price": {
      "max": {
        "field": "UnitPrice"
      }
    }
  }
}

-- avg
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "average_unit_price": {
      "avg": {
        "field": "UnitPrice"
      }
    }
  }
}

-- stats
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "all_stats_unit_price": {
      "stats": {
        "field": "UnitPrice"
      }
    }
  }
}


-- cardinality
GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "number_unique_customers": {
      "cardinality": {
        "field": "CustomerID"
      }
    }
  }
}

-- this query clause allows us to perform aggregations on a subset of documents
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

GET ecommerce_data/_search
{
  "size": 0,
  "aggs": {
    "transactions_per_day": {
      "date_histogram": {
        "field": "InvoiceDate",
        "calendar_interval": "day",
        "order": {
          "daily_revenue": "desc"
        }
      },
      "aggs": {
        "daily_revenue": {
          "sum": {
            "script": {
              "source": "doc['UnitPrice'].value * doc['Quantity'].value"
            }
          }
        },
        "number_of_unique_customers_per_day": {
          "cardinality": {
            "field": "CustomerID"
          }
        }
      }
    }
  }
}