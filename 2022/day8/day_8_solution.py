import numpy as np

# read text input and convert into numpy array matrix
def read_input(filename):
    with open(filename) as f:
        data_raw = f.read().splitlines()

    # seperate characters of substring for conversion into numpy array
    data = [[*list(map(int,string))] for string in data_raw]
    data = np.array(data)

    return data

# Part 1
# for a given numpy array, find the trees visible from the LHS
# see https://adventofcode.com/2022/day/8 for context
def visible_trees_lhs(array):
    results = array.copy()
    for r_ind, row in enumerate(array):
        for i_ind, i in enumerate(row):
            # if it's not the first tree or bigger than any other tree, it must be invisible
            # to show this set the height to -1
            if not(i_ind==0 or (i > max(results[r_ind][:i_ind]))):
                results[r_ind][i_ind] = -1

    return results

# combine views by taking the max information visible at a point from all directions
def combine_views(array_list):
    combined = array_list[0]
    for i in array_list:
        combined = np.maximum(combined, i)
    return combined

# apply visible trees in all directions and combine result
def visible_trees(filename):
    input_raw = read_input(filename)

    # transform input and apply function to represent looking from all directions
    lhs = visible_trees_lhs(input_raw)
    ts = visible_trees_lhs(input_raw.transpose())
    bs = visible_trees_lhs(input_raw[::-1,::-1].transpose())
    rhs = visible_trees_lhs((input_raw.transpose())[::-1,::-1].transpose())

    # transform back to normal orientation
    ts = ts.transpose()
    bs = bs[::-1,::-1].transpose()
    rhs = (rhs.transpose())[::-1,::-1].transpose()

    # combine results to get all visible trees
    results = combine_views([lhs, rhs, ts, bs])

    return np.count_nonzero(results >= 0)

visible_trees('input.txt')

# Part 2
# for each point in the grid, move right and check if visible
def horizontal_right_trees(array):
    results = array.copy()
    for r_ind, row in enumerate(array):
        for i_ind, i in enumerate(row):
            # if at the edge, return 0
            if len(results[r_ind][i_ind:]) == 1:
                results[r_ind][i_ind:] = 0
            else:
                view = 0
                # if not at an edge, move forwards until visibility is lost
                for j in results[r_ind][i_ind+1:]:
                    view += 1
                    if j >= i:
                        break
                results[r_ind][i_ind] = view
    return results

def tree_sight(filename):
    input_raw = read_input(filename)

    # transform input and apply function to represent score in all directions
    lhs = horizontal_right_trees(input_raw)
    ts = horizontal_right_trees(input_raw.transpose())
    bs = horizontal_right_trees(input_raw[::-1,::-1].transpose())
    rhs = horizontal_right_trees((input_raw.transpose())[::-1,::-1].transpose())

    # transform back to normal orientation
    ts = ts.transpose()
    bs = bs[::-1,::-1].transpose()
    rhs = (rhs.transpose())[::-1,::-1].transpose()

    # combine results to get all visible trees
    results = lhs * rhs * ts * bs

    return results.max()

tree_sight('input.txt')
