from typing import Iterable


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