import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Print all unique lines from sorted files in a directory in sorted order'
    )
    DIRECTORY = 'directory'
    parser.add_argument(DIRECTORY, nargs='+', help='The relative path of the directory')
    args = parser.parse_args()
    path = args[DIRECTORY]


if __name__ == '__main__':
    main()
