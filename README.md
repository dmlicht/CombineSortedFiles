# Combine Sorted Files
Have a bunch of sorted files you want to merge together into an **even bigger** sorted file?
You can use `combine_sorted` to print all of the lines from your files to the standard out then pipe them
to your new gigantic file (or log).

## Usage
sort a directory:

    python combine_sorted.py the/path/to/your/directory/filled/with/sorted/files

Get help:

    python -h

## Installation
TODO

## Dependencies

Runtime:
* python 3

Test:
* pytest

## Run Tests
If you don't have pytest installed, you can install it with:

    pip install pytest

 Then from the root directory you can run tests with:

    sh test.sh

## Analysis

Implemented Solution: Simultaneous batched file reads

Definititions:

* `F` number of files
* `L` total number of lines counted among all files
* `N` number of characters on a line

## Roadmap

[ ] Add chunked file reads (so we don't get overwhelmed in terms of memory or have to keep a million files open at once).
We currently have a **large** memory bottleneck. We are reading all of the files into memory upfront. Our memory footprint is
currently `O(LN)` where `L` is the number of lines in our dataset and `N` is the number of characters that can occur on
a line. If we switch our system to partial reads, we can bind our memory footprint at `O(F)` because we will only need
to hold some constant amount of data per file at any given moment. The best result for chunksize should be found via
profiling.

[ ] Min Heap to choose next min line. Checking for the min every time is O(F) where F is the number of files we have.
If we have a million files, this becomes problematic because we will need to examine a million elements for every line
choice. This would cause an `O(FL)` runtime. If we maintain a min heap for choosing the next lowest valued line we can
bound our combined finding/removing and inserting the next element from the chosen stream to `O(log(L))` which would
make our total runtime for this bottleneck `O(Flog(L))`

[ ] Concurrently handle reads in the background

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