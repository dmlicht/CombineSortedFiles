from typing import Generator, Sequence
import heapq

from combine_sorted.stream_queue import AscendingStreamQueue


def combine_sorted(streams: Sequence[AscendingStreamQueue]) -> Generator:
    last_seen = None

    heap = [(stream.peek(), stream) for stream in streams]
    heapq.heapify(heap)

    while len(heap) > 0:
        next_el, next_stream = heapq.heappop(heap)
        next_stream.pop()
        if not next_stream.done:
            heapq.heappush(heap, (next_stream.peek(), next_stream))

        # Don't yield a value we have before.
        # We know all duplicates will occur in a row because of sorting.
        if last_seen != next_el:
            last_seen = next_el
            yield next_el
