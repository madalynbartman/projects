PUT favorite_candy

POST favorite_candy/_doc
{
  "first_name": "Biggie",
  "candy":"Skittles"
}

GET favorite_candy/_doc/3

PUT favorite_candy/_doc/1
{
  "first_name": "LB",
  "candy": "Sour Patch Kids"
}

PUT favorite_candy/_doc/2
{
  "first_name": "Alex",
  "candy": "Air Heads"
}

PUT favorite_candy/_doc/3
{
  "first_name": "Sheldon",
  "candy": "None"
}

PUT favorite_candy/_doc/3
{
  "first_name": "Duplicate",
  "candy": "Dupe"
}  
  
PUT favorite_candy/_create/1
{
  "first_name": "Test",
  "candy": "Do not pass"
}

POST favorite_candy/_update/3
{
  "doc" : {
    "candy": "butts"
  }
}

DELETE favorite_candy/_doc/3