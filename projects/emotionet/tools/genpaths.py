#!/usr/bin/env python
# coding: utf-8
import random

def new_path():
    return (tuple(), set())

def add_to_path(path, item):
    return (path[0] + (item,), path[1] | {item,})

def find_paths(edges, start, end, path=None):
    if start not in edges:
        raise Exception('missing node: {}'.format(start))

    if path is None:
        path = new_path()
    path = add_to_path(path, start)

    unvisited_neighbors = list(edges[start] - path[1] - {end})
    if not unvisited_neighbors and len(path[0]) == len(edges) - 1:
        yield path[0]

    random.shuffle(unvisited_neighbors)
    for neighbor in unvisited_neighbors:
        for p in find_paths(edges, neighbor, end, path):
            yield p

def sample_hamiltonians(edges, num_samples_per_start_node=5000):
    cycles = {}
    nodes = list(edges.keys())
    random.shuffle(nodes)
    for n, node in enumerate(nodes):
        cycles[node] = []
        for i, path in enumerate(find_paths(edges, node, node)):
            if i > num_samples_per_start_node: #
                break
            cycles[node].append(path)
        print('Done with node {}/{}: {}'.format(n+1, len(nodes), node))
    return cycles

if __name__ == '__main__':
    from edges import edges
    import json
    cycles = sample_hamiltonians(edges, 100)
    with open('src/paths.js', 'w') as fout:
        fout.write('var hamiltonians = %s' % json.dumps(cycles, indent=2))
    print('Done.')
