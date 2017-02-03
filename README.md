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