import argparse
import os

from os.path import isfile

from stream_queue import AscendingStreamQueue
from combine import combine_sorted


def main():
    parser = argparse.ArgumentParser(
        description='Print all unique lines from sorted files in a directory in sorted order'
    )
    parser.add_argument('directory', help='The relative path of the directory')
    args = parser.parse_args()
    path = args.directory
    files = files_in_path(path)

    streams = [AscendingStreamQueue(open(file).read().splitlines()) for file in files]
    for line in combine_sorted(streams):
        print(line)


def files_in_path(path):
    for ff in os.listdir(path):
        full_path = os.path.join(path, ff)
        if isfile(full_path):
            yield full_path


if __name__ == '__main__':
    main()
