# Database Sharding
This folder contains small application of using horizontal database sharding.

Database sharding is useful when data becomes huge and becomes a bottleneck for read/write operations. In such cases, it is useful to split the data among several nodes so that each node is run individually.

## Advantages:
- Increases scalability, read and write throughput
- High availability (if one node fails, other nodes still remain and can fetch atleast some data)
