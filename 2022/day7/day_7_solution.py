def read_input(filename):
    with open(filename) as f:
        data = iter(f.read().splitlines())
    return data

# set up a 'stack' of open directories
# save list of sizes of all directories
# once a directory is parsed and closed, add its size to the list of sizes
def get_dir_sizes(raw_input):
    sizes = []
    stack = [0]
    # while loop - as long as there are still nonclosed directories
    while stack:
        line = next(raw_input, "$ cd ..")
        # closing a directory - remove from the 'stack' and add it to the list of 'sizes'
        if line == "$ cd ..":
            subdir = stack.pop()
            if stack:
                sizes.append(subdir)
                stack[-1] += subdir
        # changing into a new subdir - add this dir to the 'stack'
        elif '$ cd ' in line:
            stack.append(0)
        # if displaying a file add its size to the current directory (end of the stack)
        elif line[:3] not in ['dir', '$ l']:
            size, _ = line.split()
            stack[-1] += int(size)
    return sizes

raw_input = read_input("input.txt")
sizes = get_dir_sizes(raw_input)

# Part 1
print(sum(d for d in sizes if d <= 100000))

# for part 2, sort the sizes and work out
sizes = sorted(sizes)
space_needed = 30000000 + max(sizes) - 70000000

print(min(d for d in sizes if d >= space_needed))
