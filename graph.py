class Graph:
    def __init__(self, v_quantity):
        self.__neighbors = dict()
        for v_idx in range(v_quantity):
            self.__neighbors[v_idx + 1] = set()

    def set_neighbor(self, vertex, neighbor):
        self.__neighbors[vertex + 1].add(neighbor)

    def get_neighbors(self, vertex):
        return frozenset(self.__neighbors[vertex])

    def get_vertexes(self):
        return self.__neighbors.keys()

    @staticmethod
    def read_from(filename):
        with open(filename) as f:
            v_quantity = int(f.readline())
            g = Graph(v_quantity)
            for v_idx in range(v_quantity):
                line = f.readline()
                neighbors = map(lambda x: int(x), line.split())
                for neighbor in neighbors:
                    g.set_neighbor(v_idx, neighbor)
        return g
