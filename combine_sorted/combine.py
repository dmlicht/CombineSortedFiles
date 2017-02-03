from typing import List, Generator, Sequence
import heapq

from combine_sorted.stream_queue import StreamQueue


def combine_sorted(streams: Sequence[StreamQueue]) -> Generator:
    last_seen = None

    heap = [(stream.peek(), stream) for stream in streams]
    heapq.heapify(heap)

    while len(heap) > 0:
        ## TODO: if you have millions of files this check can become a bottle neck, but can be improved by storing peeked values in a min heap
        next_el, next_stream = heapq.heappop(heap)
        next_stream.pop()
        # next_stream = get_next_stream(streams)
        # next_el = next_stream.pop()
        if not next_stream.done:
            heapq.heappush(heap, (next_stream.peek(), next_stream))

        # Don't yield a value we have before.
        # We know all duplicates will occur in a row because of sorting.
        if last_seen != next_el:
            last_seen = next_el
            yield next_el



def get_next_stream(streams: List[StreamQueue]) -> StreamQueue:
    lowest_next_el_index = min(range(len(streams)), key=lambda x: streams[x].peek())
    return streams[lowest_next_el_index]
