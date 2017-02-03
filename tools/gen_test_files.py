import random
import string
import argparse

N_FILES = 1000000
MAX_ROW_LENGTH = 100
MAX_N_ROWS = 1000
TEST_FILE_DIR = "../example/"


def gen_random_line(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(0, 1 + length))


def gen_random_block(n_lines, max_line_length):
    return [gen_random_line(random.choice(range(0, 1 + max_line_length))) for _ in range(0, 1 + n_lines)]


# TODO: Add command args
def main():
    parser = argparse.ArgumentParser(
        description='Generate N random text files to test our sorter'
    )
    parser.add_argument('n', type=int, help='Number of files to generate')
    args = parser.parse_args()
    n_files = args.n

    for ii in range(N_FILES):
        if ii % 200 == 0: print("generated: ", ii)
        row_length = random.choice(range(0, MAX_ROW_LENGTH))
        n_rows = random.choice(range(0, MAX_N_ROWS))
        block = sorted(gen_random_block(row_length, n_rows))
        with open(TEST_FILE_DIR + "test" + str(ii) + ".txt", 'w') as ff:
            ff.writelines('\n'.join(block))


if __name__ == '__main__':
    main()
