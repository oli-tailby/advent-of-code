# Function retaining only odd-indexed elements and converting to int
# Used in input_clean
def odd_index_ints(string):
    odd_index = string[1::2]
    output = tuple(map(int, odd_index))
    return output

# Data cleaning from AOC format
# See https://adventofcode.com/2022/day/5
def input_clean(filename):
    with open(filename) as f:
        input_raw = f.read().splitlines()

    sep = input_raw.index('')
    stacks_raw, label, procedure_raw = input_raw[:sep-1], input_raw[sep-1], input_raw[sep+1:]

    stacks = [[] for x in range(int(label[-1]))]

    for row in stacks_raw:
        for ind, box in enumerate(row):
            # If the index matches a stack label and isn't empty, add to cleaned stack data
            if (ind-1 in [label.index(x) for x in label if (x!=' ')]) & (box != ' '):
                stacks[int(label[ind-1])-1].insert(0, box)

    # Create 3-tuples for procedure data
    # (move n boxes, from here, to here)
    # See https://adventofcode.com/2022/day/5 for context
    procedure_raw = [i.split(' ') for i in procedure_raw]
    procedure = list(map(odd_index_ints, procedure_raw))

    return stacks, procedure

def apply_procedure(stacks, procedure):
    for (a,b,c) in procedure:
        # Move (a) from (b) to (c)
        move_boxes = stacks[b-1][-a:]
        stacks[c-1] += list(reversed(move_boxes))
        stacks[b-1] = stacks[b-1][:-a]
    return stacks

# Part 1

def get_top_boxes(filename):
    stacks, procedure = input_clean(filename)
    final_stacks = apply_procedure(stacks, procedure)
    output = []
    for i in final_stacks:
        output.append(i[-1])

    return ''.join(output)

get_top_boxes('input.txt')

# Part 2

def apply_procedure_nonreversed(stacks, procedure):
    for (a,b,c) in procedure:
        # Move (a) from (b) to (c)
        move_boxes = stacks[b-1][-a:]
        stacks[c-1] += list(move_boxes)
        stacks[b-1] = stacks[b-1][:-a]
    return stacks

def get_top_boxes_nonreversed(filename):
    stacks, procedure = input_clean(filename)
    final_stacks = apply_procedure_nonreversed(stacks, procedure)
    output = []
    for i in final_stacks:
        output.append(i[-1])

    return ''.join(output)

get_top_boxes_nonreversed('input.txt')
