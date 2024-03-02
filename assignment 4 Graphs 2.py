class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, source, visited):
        visited[source] = True
        print(source, end=' ')

        for neighbor in self.adj_list[source]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self):
        visited = [False] * self.n

        for vertex in range(self.n):
            if not visited[vertex]:
                self.dfs(vertex, visited)

# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)

g.dfs_traversal()  # Output: 0 1 3 4 2 5
