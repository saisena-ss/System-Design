# Cache

##### Why do we need cache?
 - When the database is huge and the traffic or concurrent requests are huge, number of read or write calls would be huge and the server might not handle well (increases latency). One option is to scale the server. But another option is to reduce the calls to the database by storing most frequently accessed records in cache for faster access. By storing in cache, number of calls to the database is reduced.

 - L1 Cache >> L2 Cache >> RAM >> Disk (in terms of speed, and in terms of cost, it is vice versa).


 Request ----> DB 
         <----

#### Cache Eviction
- When cache is full, you would want to delete some entries and make space for new ones, removing present entries -- cache eviction.

##### Types:
- Least Recently Used
- Most Recently Used
- Least Frequently Used
- Random Replacement
- FIFO (First In First Out)
- LIFO (Last In First Out)



#### Cache Invalidation
- When a record in the database is updated or deleted, data present in cache might be not uodated or might not be consistent with database, in that case we need to invalidate the cache.

- Write Through Cache - may increase write latency as both cache and db needs to be updated or written
- Write Around Cache - Directly write in database, invalidate the record in cache, might lead to more cache miss if recently written data is read again.
- Write Back Cache - Write to the cache, Cache updates the database asynchronously. Problem is when cache fails or db crashes (power failure) before data is not written to the db, this results in inconsistent data.

#### Advantages:
- Better performance
- Lesser load on database

#### Disadvantages:
 - Increases complexity of the system
 - Need to take care of cache eviction and invalidation for maintainig consistency.

#### Read Strategies:
1. Cache Aside: Application server reads the data from database if data is not present in the cache, and writes it to the cache. Disadvantage is complexity is shifted to application server handling eviction and invalidation policy, and maintaining data consistency.
2. Read Through: Instead of getting data through server, cache fetches data from database and returns to the server.
3. Refresh Ahead: Each item has an expiration time. Based on the expiration time, prefetch the data and store it in cache. If the data in cache is frequently accessed, instead of expiring it, it's expiring time can be increased  - this is checked using refresh ahead factor and time to live.


#### Types of Cache:
- Distributed Cache : Data is distributed across multiple nodes exclusively (no intersection of data), similar to database sharding.
- Gloabl Cache : Just one node to store all the data in cache.
- Contnet Distribution Network : Used to store static data like HTML, images

#### When not to use Cache?
- If access time from cache is equivalent to access time of database, then there is no point in using cache or change caching strategy.
- If there are more updates then cache might be out of sync.