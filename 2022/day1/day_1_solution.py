# Extract input and split by newline
def get_input(filename):
    with open(filename) as f:
        cals_input = f.read().splitlines()

    return cals_input

# Index through calorie counts and sum for each elf. Assign a new elf on a blank line
def elf_count_cals(cals_input):
    ind=0
    elf_cals=[0]
    for i in cals_input:
        if i=='':
            ind += 1
            elf_cals.append(0)
        else:
            elf_cals[ind] += int(i)

    return elf_cals

# Sort elves descending and sum the top n values
def sum_top_n(input_list, n):
    list_sorted = sorted(input_list, reverse=True)
    sum_top_n = sum(list_sorted[0:n])

    return sum_top_n

# Get input
cals_input = get_input('input.txt')

# Part 1
elf_cals = elf_count_cals(cals_input)
sum_top_n(elf_cals, 1)

# Part 2
elf_cals = elf_count_cals(cals_input)
sum_top_n(elf_cals, 3)
