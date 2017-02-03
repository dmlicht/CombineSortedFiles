from typing import List, Generator, Iterable


class StreamQueue:
    """ Like a generator, but you can peek before you take an element."""

    def __init__(self, src: Iterable):
        self.src = src
        self.iterator = iter(src)
        self.done = False
        self._get_next()

    def peek(self):
        if self.done:
            raise StopIteration

        return self.next

    def pop(self):
        if self.done:
            raise StopIteration

        tmp = self.next
        self._get_next()
        return tmp

    def _get_next(self):
        try:
            self.next = next(self.iterator)
        except StopIteration:
            self.done = True


# We can also just make a version where we can pass in constraints instead of making different subclasses.
# But it's probably too much work for this little script.
class AscendingStreamQueue(StreamQueue):
    """ Like a StreamQueue but it raises an error if inputs are not sorted """

    def __init__(self, src):
        self.next = ""  # this is sort of a hack
        super().__init__(src)

    def _get_next(self):
        try:
            prev = self.next
            self.next = next(self.iterator)
            if prev > self.next:
                raise Exception("Input not sorted properly")

        except StopIteration:
            self.done = True


def combine_sorted(streams: List[StreamQueue]) -> Generator:
    last_seen = None
    while len(streams) != 0:
        ## TODO: if you have millions of files this check can become a bottle neck, but can be improved by storing peeked values in a min heap
        next_stream = get_next_stream(streams)
        next_el = next_stream.pop()
        if next_stream.done:
            streams.remove(next_stream)

        # Don't yield a value we have before.
        # We know all duplicates will occur in a row because of sorting.
        if last_seen != next_el:
            last_seen = next_el
            yield next_el


def get_next_stream(streams: List[StreamQueue]) -> StreamQueue:
    lowest_next_el_index = min(range(len(streams)), key=lambda x: streams[x].peek())
    return streams[lowest_next_el_index]
