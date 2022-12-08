# From text file, take the minimum and maximum task number for each elf
# Sorted in sublists - each pair is a list element, and each sublist contains their min and max task id
def tasks_input(filename):
    with open(filename) as f:
        pair_tasks = f.read().splitlines()

    tasks = [i.split(',') for i in pair_tasks]

    for j, task in enumerate(tasks):
        tasks[j] = [map(int,n.split('-')) for n in task]

    return tasks

# Part 1
# Count the tasks in which one of an elf pair's tasks is entirely contained by the other's
# See https://adventofcode.com/2022/day/4
def count_contained(tasks):
    total = 0
    for [[a,b],[m,n]] in tasks:
        a_in_b = (a>=m)&(b<=n)
        b_in_a = (m>=a)&(n<=b)
        if (a_in_b | b_in_a):
            total += 1
    return total

def count_contained_tasks(filename):
    tasks = tasks_input(filename)
    count = count_contained(tasks)
    return count

count_contained_tasks('input.txt')

# Part 2
# Count the tasks in which an elf pair's tasks are overlapped by the other
# See https://adventofcode.com/2022/day/4
def count_overlap(tasks):
    total = 0
    for [[a,b],[m,n]] in tasks:
        if not ((m>b)|(n<a)):
            total += 1
    return total

def count_overlap_tasks(filename):
    tasks = tasks_input(filename)
    count = count_overlap(tasks)
    return count

count_overlap_tasks('input.txt')
