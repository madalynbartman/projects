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

