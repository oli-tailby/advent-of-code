import numpy as np

class Graph:
    def __init__(self, vertices):
        self.edges = {v: [] for v in range(vertices)}

    def add_edge(self, u, v, weight=1):
        self.edges[u].append(v)

    def bfs(self, start, ends):
        explored = []
        queue = [[start]]
        if start in ends: return 0

        while queue:
            path = queue.pop(0)
            node = path[-1]
            # move through nodes closest first
            if node not in explored:
                neighbours = self.edges[node]
                # explore neighbors
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # if an acceptable end is reached, return the route
                    if neighbour in ends:
                        return len(new_path)-1
                # mark node as explored
                explored.append(node)
        return len(new_path)-1

def read_input(filename, part):
    def adj_points(i_x,i_y,j_x,j_y):
        adj_x = ((abs(i_x-j_x)==1) & (abs(i_y-j_y)==0))
        adj_y = ((abs(i_x-j_x)==0) & (abs(i_y-j_y)==1))
        return (adj_x | adj_y)

    with open(filename) as f:
        data = f.read().splitlines()

    data = np.array(list(map(list, data)))
    steps = Graph(data.size)

    # set end options based on part (actually using the start, since we run backwards)
    if part==2:
        data[data=='S'] = 'a'
        ends_init = np.where(data=='a')
        ends = []
        for i in range(len(ends_init[0])):
            ends.append(data.shape[1]*ends_init[0][i] + ends_init[1][i])
    else:
        ends = np.where(data=='S')
        ends = (data.shape[1]*ends[0] + ends[1])
        data[data=='S'] = 'a'
    # set start point (actually using the end, since we run the algorithm backwards)
    start = np.where(data=='E')
    data[data=='E'] = 'z'
    start = (data.shape[1]*start[0] + start[1])[0]

    for i in range(data.size): # compare each point to other points and add an edge where possible
        (i_x, i_y) = (i % data.shape[1], int(i/data.shape[1]))
        for j in range(data.size):
            (j_x, j_y) = (j % data.shape[1], int(j/data.shape[1]))
            if adj_points(i_x,i_y,j_x,j_y): # if points suitably close...
                if ord(data[j_y,j_x])-ord(data[i_y,i_x]) <= 1: # ...and the step up is small enough...
                    steps.add_edge(j, i) # ...set the reverse as the weighting (as we run backwards)

    return steps, start, ends, data

def shortest_path(filename, part=1):
    steps, start, ends, _ = read_input(filename, part)
    return steps.bfs(start, ends) # run bfs backwards to accepted 'ends' (starts of the trail)

shortest_path('input.txt')
shortest_path('input.txt', part=2)
