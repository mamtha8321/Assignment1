from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, source):
        visited = [False] * self.n
        queue = deque()

        visited[source] = True
        queue.append(source)

        while queue:
            u = queue.popleft()
            print(u, end=' ')

            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)

g.bfs(0)  # Output: 0 1 2 3 4 5
