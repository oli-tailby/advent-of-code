def rucksack_input(filename):
    with open(filename) as f:
        sacks = f.read().splitlines()

    return sacks

# Split list into two equal length sublist
# Assumes even list length
def split_sacks(sacks):
    split_sacks = [i[int(len(i)/2):], i[:int(len(i)/2)]] for i in sacks]
    return split_sacks

# Return common items in all sublists of the input
def common_items(sack):
    common = set(sack[0]).intersection(*sack)
    return list(common)

# Return priority (int) of a character by AOC rules
def priority(item):
    priority = ord(item.lower()) - 96
    if item.islower():
        return priority
    else:
        return priority + 26

# Part 1
# Calculate the sum of priorities from a text file in given AOC format
# See https://adventofcode.com/2022/day/3
def sum_priority(filename):
    total = 0
    sacks = rucksack_input(filename)
    split = split_sacks(sacks)
    for i in split:
        common = common_items(i)
        total += priority(common[0])
    return total

sum_priority('input.txt')

# Part 2
def get_groups(sacks):
    groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    return groups

# Calculate the sum of group priorities from a text file in given AOC format
# See https://adventofcode.com/2022/day/3
def group_sum_priority(filename):
    total = 0
    sacks = rucksack_input(filename)
    groups = get_groups(sacks)
    for i in groups:
        common = common_items(i)
        total += priority(common[0])

    return total

group_sum_priority('input.txt')
