import argparse
import os

from os.path import isfile


def main():
    parser = argparse.ArgumentParser(
        description='Print all unique lines from sorted files in a directory in sorted order'
    )
    parser.add_argument('directory', help='The relative path of the directory')
    args = parser.parse_args()
    path = args.directory
    files = files_in_path(path)

    for file in files:
        
        print(open(file).readlines())


def files_in_path(path):
    for ff in os.listdir(path):
        full_path = os.path.join(path, ff)
        if isfile(full_path):
            yield full_path


if __name__ == '__main__':
    main()
