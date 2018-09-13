#!/usr/bin/python3

import sys
from queue import Queue
from argparse import ArgumentParser
from graph import Graph


def make_bfs(g: Graph):
    queue = Queue()
    visited = set()
    for v_idx in g.get_vertexes():
        if v_idx in visited:
            continue
        queue.put(v_idx)
        while (not queue.empty()):
            curr_v = queue.get()
            if curr_v in visited:
                continue
            visited.add(curr_v)
            yield curr_v
            for neighbor_idx in g.get_neighbors(curr_v):
                if neighbor_idx in visited:
                    continue
                queue.put(neighbor_idx)


def init_parser():
    parser = ArgumentParser(description="Breadth First Search")
    parser.add_argument("source_file", action="store")
    return parser


def main():
    parser = init_parser()
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    g = Graph.read_from(args.source_file)
    BFS_set = make_bfs(g)
    for v_idx in BFS_set:
        print(v_idx)


if __name__ == '__main__':
    main()
