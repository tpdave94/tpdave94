class Graph:
    """Graph Module."""
    def __init__(self, v):
        self.v = 0
        self.e = 0
        self.adj = [[] for i in range(self.v)]

    def add_edge(self, v, w):
        self.e += 1
        self.adj[v].append(w)
        self.adj[w].append(v)

    def df_traversal(self, v, visited):
        visited[v] = True

        for i in self.adj[v]:
            if not visited[v]:
                self.df_traversal(v, visited)

    def is_connected(self):
        visited = [False] * self.v
        self.df_traversal(0, visited)
        return True if all(self.visited) else False

    def isTree(self):
        return self.is_connected() and self.e == self.v -1


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

