#!/usr/bin/env python
# coding: utf-8

# Define the graph with nodes and edges
Graph_nodes = {
    "P" : [("Q", 4), ("R", 2)],
    "Q" : [("S", 5), ("T", 10)],
    "R" : [("T", 8), ("U", 6)],
    "S" : [("V", 7)],
    "T" : [("V", 4), ("W", 6)],
    "U" : [("W", 3), ("X", 9)],
    "V" : [("Y", 3)],
    "W" : [("Y", 2)],
    "X" : [("Z", 5)],
    "Y" : [("Z", 1)]
}

# Function to get neighbors of a node
def get_neighbors(v):
    return Graph_nodes.get(v, None)

# Heuristic function
def h(n):
    H_dist = {
        "P" : 12,
        "Q" : 10,
        "R" : 8,
        "S" : 7,
        "T" : 6,
        "U" : 5,
        "V" : 4,
        "W" : 3,
        "X" : 2,
        "Y" : 1,
        "Z" : 0
    }
    return H_dist[n]

# A* algorithm implementation
def A_star_algo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = min(open_set, key=lambda x: g[x] + h(x))
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found: {}".format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

    print("Path does not exist!")
    return None

# Run the A* algorithm
A_star_algo("P", "Z")