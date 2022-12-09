# read text input and convert into numpy array matrix
def read_input(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def head_move_pos(old_pos, instr):
    (h_x, h_y) = old_pos

    # define the new head coordinates from the instruction
    if instr == 'R':
        h_x+=1
    elif instr == 'L':
        h_x-=1
    elif instr == 'U':
        h_y+=1
    elif instr == 'D':
        h_y-=1

    new_pos = (h_x, h_y)

    return new_pos

def tail_move_pos(old_pos, head_pos):
    (t_x, t_y) = old_pos
    (h_x, h_y) = head_pos

    x_dist = h_x - t_x
    y_dist = h_y - t_y

    # if far enough from head, move
    if (abs(x_dist)>1) | (abs(y_dist)>1):

        # if at a diagonal move in both axis
        if (abs(x_dist) > 0) & (abs(y_dist) > 0):
            if x_dist > 0:
                t_x += 1
            else:
                t_x -= 1
            if y_dist > 0:
                t_y += 1
            else:
                t_y -= 1

        # if on a row move in the direction of the head
        elif (x_dist==0) | (y_dist==0):
            if x_dist > 0:
                t_x += 1
            elif x_dist < 0:
                t_x -= 1
            elif y_dist > 0:
                t_y += 1
            elif y_dist < 0:
                t_y -= 1

    new_pos = (t_x, t_y)

    return new_pos

def get_all_positions(filename, n_tails=1):

    data = read_input(filename)
    head_pos = (0,0)
    tail_pos = [(0,0)]*n_tails # tailpos[i] represents the location of the ith tail
    all_positions = set()

    # for each instruction...
    for step in data:
        instr, rep = step.split()
        # repeat the specified number of times...
        for i in range(int(rep)):
            # update head and first tail position
            head_pos = head_move_pos(head_pos, instr)
            tail_pos[0] = tail_move_pos(tail_pos[0], head_pos)
            for i in range(1,n_tails):
                # for each remaining tail, use the previous tail as the head
                tail_pos[i] = tail_move_pos(tail_pos[i], tail_pos[i-1])
            # store the location of the last tail
            all_positions.add(tail_pos[n_tails-1])

    return len(all_positions)

# Part 1
get_all_positions('input.txt', 1)

# Part 2
get_all_positions('input.txt', 9)
