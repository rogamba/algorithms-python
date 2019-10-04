# Repasar

# Algorithms and DS

### Recursion
- change making: memoization per item qty inside the path
- phone numbers: all combinations for every position
- powersets: elimination by position (backtracking)

### Arrays
- substring: hashtable of key, array of indexes, path of indexes
- string reversal: stack or pointers
- palindrome: pointers beginning and end
- cinema seats

### Linked Lists
- reverse inplace a linked list O(1) memory

### Sorting and searching
- sort tuples by value

### Graph
- Depth First Search
- Breath First Search
- Shortest path

# System Design
- Users per day of month -> to get the QPS (Queries per second)
- Calculate storage through Data Capacity Model
  - Denormalized model or normalized one
- Calculate I/O and size of storage to decide the technology and scale
  - SQL if atomicity is priority
  - NoSQL if scalability is priority
    - CAP (Consistency, Availability, Partition Tolerance)
- Suggest a cache layer if applies
- Cache access/refresh
  - Write through: In the same request writes to cache and DB
  - Write around: On write request the data is store in the DB, only on reads it checks the Cache, 
    if it doesn't have the data it fetches from DB and stores it
  - Write back: Writes to cache and uses a service to sync the DB
- Cache eviction (LRU)

### URL Shortener
- Base62 algorithm:
- MD5 hash: takes the text and creates a hash, there are more collisions 
- Using Zookeeper to tell the counter range for the appservers

### Rate Limiting
- Token Bucket (memory efficient): stores user, last accessed, counter of remaining requests for a given period of time
- Leaky Bucket: uses a queue and a loop that process requests at a given rate to protect from overloading the server
- Sliding logs
- Sliding window counter: Array of the last n number of requests with their counter [ (timestamp, counter), (timestamp, counter) ]
  update the array every minute, count all the counters
On Scale
* Inconsistency -> solving it with sticky session on the LB (redirecting the user always to the same rate limiting service)
* Race condition -> using locks on the accessed keys so the key can't be accessed more than once on update

### Auto suggestion
- Tries

### Consistent Hashing 
- [Pending]

### Distributed data stores
CAP Theorem
- Consistency
- Availability
- Partition Tolerant
* Master-Slave scale: Master handles writes and slaves handle read, there can be inconsistency
* Sharding: Paritition data and assign key ownerships, joins are super expesive

### Distributed cache
- Features and estimations
- Cache access patterns
  - Write through: In the same request writes to cache and DB
  - Write around: The request only stores on the DB and on the read it Checks if Cache has the data 
  - Write back: Writes to cache and uses a service to sync the DB
- LRU (Least Recently Used)
  - It's implemented with a d ouble linked list
  - The bucket of the hash function simply points to the address of the linked list node, so there's no need of duplication
- Persistancy:
  - Snapshots
  - Log reconstruction
- Availability
  - Master-slave

### Geospacial data
- Geohashes to have constant access time

### Bloom Filter
- Probabilistic data structure for testing weather an element is NOT in a list
  - Responds:
  - Not present: 100% certainty
  - Present: less than 100% (not sure)

  ### Locks
  - Locks: forbid access to a section of the memory for a particular process
  - Mutex: like locks but forbid access to multiple processes