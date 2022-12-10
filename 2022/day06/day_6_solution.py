# Data cleaning from AOC format
# See https://adventofcode.com/2022/day/5
def distict_run(filename, n):
    input_raw = open(filename).read()

    for ind, _ in enumerate(input_raw):
        test = input_raw[ind:ind+n]
        if len(test) == len(set(test)):
            return ind+n

distict_run('input.txt', 4)
distict_run('input.txt', 14)
