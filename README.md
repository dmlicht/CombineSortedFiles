# Combine Sorted Files



## Roadmap

### File IO

- Add basic file reads
- Add chunked file reads
- Multithreading reads in the background


- Min Heap to choose next min line
-


## Analysis

### Implemented Solution: Simultaneous batched file reads

### Second choice: In Memory Data Store (probably `redis`)
Read files and dump all lines as entries into an in memory data store.

Advantages:
  - This solution seems to be the least work, and will probably be reasonably efficient out of the box.
  We can let the datastore do our management and sorting of lines.

Disadvantages:
  - We have store all of our data in memory or on disk a second time
  - IO may take a long time interacting with the datastore.
  Though to be honest, it's tough to tell which solution will take longer without profiling an example.
  I probably wont have time to build both today, though it wouldn't be unreasonable to prototype both methods
  in one day for a production tool.

### Considered Solutions
- read one file at a time, maintain a sorted list of all lines currently seen.
- Open all files at once and read line by line