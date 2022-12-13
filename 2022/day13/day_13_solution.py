def read_input(filename, part=1):
    with open(filename) as f:
        data = f.read().splitlines()

    pairs = []
    if part==1: # for first part, sort into pairs
        for i in range(int((len(data)+1)/3)):
            pairs.append((eval(data[3*i]), eval(data[3*i+1])))
    else: # for second part create a list of each packet
        for i in range(int((len(data)+1)/3)):
            pairs.append(eval(data[3*i]))
            pairs.append(eval(data[3*i+1]))

    return pairs

def compare_pair(pair):
    (l1, l2) = pair
    # if both integer values, compare size:
    if (type(l1) is int) and (type(l2) is int):
        if l1<l2: return 1
        elif l1>l2: return -1
        else: return 0
    else: # otherwise, if only one is int convert to list
        if type(l1) is int: l1=[l1]
        if type(l2) is int: l2=[l2]
    for a, b in zip(l1,l2): # call function recursively
        r = compare_pair((a, b))
        if r != 0: # if conclusive, return result
            return r
    # if previous tests were inconclusive return results based on length
    if len(l1) < len(l2):
        return 1
    elif len(l1) == len(l2):
        return 0
    else:
        return -1

# Part 1
def compare_all_pairs(filename):
    ind_total = 0
    pairs = read_input(filename)
    for ind, pair in enumerate(pairs):
        if compare_pair(pair)==1: ind_total += ind+1
    return ind_total

compare_all_pairs('input.txt')

# Part 2
def count_before_dividers(filename, dividers):
    key = 1
    packets = read_input(filename, part=2)
    for div in dividers: # for each divider count the packets before it
        ind = 1
        for packet in packets:
            if compare_pair((packet, div))==1:
                ind += 1
        key *= ind
        packets.append(div)
    return key

count_before_dividers('input.txt', [[[2]], [[6]]])
