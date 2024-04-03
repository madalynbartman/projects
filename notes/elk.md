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