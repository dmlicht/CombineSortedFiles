from typing import List, Generator, Sequence

from src.stream_queue import StreamQueue


def combine_sorted(streams: Sequence[StreamQueue]) -> Generator:
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
