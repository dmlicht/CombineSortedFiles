import random
import string

N_FILES = 100
MAX_ROW_LENGTH = 100
MAX_N_ROWS = 1000
TEST_FILE_DIR = "../example/"


def gen_random_line(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def gen_random_block(n_lines, max_line_length):
    return [gen_random_line(random.choice(range(max_line_length))) for _ in range(n_lines)]


def main():
    for ii in range(N_FILES):
        row_length = random.choice(range(MAX_ROW_LENGTH))
        n_rows = random.choice(range(MAX_N_ROWS))
        open(TEST_FILE_DIR + "test" + str(ii) + ".txt", 'w').writelines('\n'.join(gen_random_block(row_length, n_rows)))


if __name__ == '__main__':
    main()
