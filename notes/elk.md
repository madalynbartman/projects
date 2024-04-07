*******************************************
Elastic Stack Essentials acloud guru
*******************************************

Beats -> logstash -> elasticsearch -> kibana

architecture of project in this course:
Beats -> elasticsearch -> kibana

beats:
lightwieght data shippers

logstash: 
data processing pipeline
input: beats, tcp, etc
Filter: JAON, XML< grok, mutate, etc
output: elasticsearch, cloudwatch, graphite, kafka, s3, etc

elasticsearch:
search and analytics engine
data node -> master node -> coordinating node & ingest node
sharding (elasticsearch):
primary & replication
breaking it up into shards allows us to spread the index out across the cluster (gives us the benefit of parallel computing and distributed storage)
replicating wach of these shards gives us the advantage of better search throughput
(more copies of the data to search and gives the advantage of redundancy & fault tolerance)

kibana:
discover, visualize, dashboard, and manage

*******************************************
Complete Guide to Elasticsearch Udemy
by Bo Anderson
*******************************************
Elasticsearch use cases:

Application performance management (APM) 
Aggrigations
Analyze data
Capacity mgmt
anomality detection
Search

This course mainly focuses on search

Documents:
Data is stored as documents (similar to rows in relational databases) 
Documents contain fields (similar to columns)
A document is essentially a json object

Since elasticsearch is distributed by nature, it's scales well and is fast

Overview of elastic stack:
developed and maintained by the same company

Kibana:
analytics and visualtization platform
change detection & forcasting
can configure elasticsearch authentication & authorization 

Logstash:
process logs from apps and send to elasticsearch
data processing pipeline. 
data is handled as events and can be anything of your choice
events are processed y logstashed and sent to various outputs (also called stashes)

A logstash pipeline consists of three parts or stages:
inputs, filters, and outputs

Each stage can make use of a plugin
ex: input plugin can be a file
ex: filter plugins can be csv
ex: output plugin can be kafka

A logstash pipeline is defined in a proprietary markup format that is similar to JSON
Not just another markup language, you can add conditional statements to it and make the pipline dynamic.

X-PAK:
Adds additional features to Elasticsearch & Kibana
Security
Adds authentication and authorization (can integrate with LDAP, and AD plus manage users & roles)
monitor performance metrics for the ELK stack
alerting

*********************************************************
Mini Beginner's Crash Course to Elasticsearch and Kibana
by Lisa Jung
*********************************************************

Sharding: 
When you create an index, one shard is created by default and assigned to a node. 
Shard is where documents are stored
The number of documents a shard can hold depends on the capacity of the node
Distributing data across shards allows us to search shards in parallel which makes the search quicker
Can store copies (aka replica shards) of original shards (aka primary  shards) to increase fault tolerance (back ups) and improve performance of shards cause they can be searched too (like a read replica in a sense)

Installation:
Self managed 
Cloud services (SaaS & serverless) 30 day free trial
Orchestration services (intermediate solution b/t self managed and serverless in terms of complexity) They are: Elastic Cloud Enterprise or Elastic Cloud on Kubernetes
Orchestration services allow you to centrally manage multiple deployments on your infrastructure 

Elastic cloud:
Host elastic services

The Elastic Stack:
Kibana: explore, visualize, engage
Elasticsearch: store, search, analyze
Integrations: connect, collect, alert

Elastic search:
heart of the elastic stack
search & analytics engine that powers the search functions in a lotta mainstream apps
Elastic is a search company
Fast, scalable, relevant results
True positives are relevant documents that are returned to the user
False positives are irrelevant documents that are returned to the user

Precision and recall:
Precision and relevance measure the relevance of search results
Calculated as: 
true positives / (true positives + false positives) = precision
Recall is calculated as:
True positives / (true positives + false negatives) = recall
Precision and recall are inversely related like this:
recall = retrieve as many results as possible even if documents arent a perfect match
precision = make the retrieved results a perfect match to the query, even if it means returning less content 
Precision & recall determine which documents are included in the search results but precision and recall do not determine which of the returned documents are more relevant compared to the other!

Ranking:
Ranking refers to the ordering of the results (from most relevant results at the top, to least relevant at the bottom)
determined by a scoring algo
each result is given a score 
The score is a value that represents how relevant a document is to that specific query
A score is computed for each document that is a hit
A score is computed from multiple factors but only focusing on two in this course:
Term frequency and inverse document frequency determines how many times each search term appears in a document.
If search terms are found in high frequency in a document, the document is considered more relvenat to the search query.


