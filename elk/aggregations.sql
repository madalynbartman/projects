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
            "Country": "Germany"
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