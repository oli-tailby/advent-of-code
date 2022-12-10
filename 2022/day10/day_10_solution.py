# read text input and convert into numpy array matrix
def read_input(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def run_cycles(data):
    cycles_during = []
    current = (0,1)
    for instr in data:
        if instr == 'noop':
            current = (current[0]+1, current[1])
            cycles_during.append(current)
        else:
            current = (current[0]+1, current[1])
            cycles_during.append(current)

            current = (current[0]+1, current[1])
            addx = int(instr.split()[-1])
            cycles_during.append(current)
            current = (current[0], current[1]+addx)

    return cycles_during

# Part 1
def sum_cycles_during(filename, ns):
    data = read_input(filename)
    cycles_during = run_cycles(data)
    total = 0
    for n in ns:
        total += cycles_during[n-1][1] * n

    return total

sum_cycles_during('input.txt', [20, 60, 100, 140, 180, 220])

# Part 2
def print_terminal(filename, size):
    data = read_input(filename)
    cycles_during = run_cycles(data)
    output = ['.']*len(cycles_during)
    for (cyc, x) in cycles_during:
        line_pos = cyc % size[0]
        if abs(line_pos-x-1) <= 1:
            output[cyc-1] = '#'

    for n in range(size[1]):
        line = output[n*size[0]:(n+1)*size[0]-1]
        print(*line)

print_terminal('input.txt', (40, 6))
