#!/usr/bin/python3

import sys
from queue import LifoQueue as Stack
from argparse import ArgumentParser
from graph import Graph


def make_dfs(g: Graph):
    stack = Stack()
    visited = set()
    for v_idx in g.get_vertexes():
        if v_idx in visited:
            continue
        stack.put(v_idx)
        while (not stack.empty()):
            curr_v = stack.get()
            stack.put(curr_v)  # just peek, not pop
            has_unvisited_neighbor = False
            if curr_v not in visited:
                yield curr_v
                visited.add(curr_v)
            for neighbor_idx in g.get_neighbors(curr_v):
                if neighbor_idx in visited:
                    continue
                stack.put(neighbor_idx)
                has_unvisited_neighbor = True
                break
            if has_unvisited_neighbor:
                continue
            stack.get()  # pop


def init_parser():
    parser = ArgumentParser(description="Depth First Search")
    parser.add_argument("source_file", action="store")
    return parser


def main():
    parser = init_parser()
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    g = Graph.read_from(args.source_file)
    DFS_set = make_dfs(g)
    for v_idx in DFS_set:
        print(v_idx)


if __name__ == '__main__':
    main()
