from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def has_cycle(self):
        visited = set()
        rec_stack = set()

        for v in self.adj_list:
            if self.dfs(v, visited, rec_stack):
                return True

        return False

    def dfs(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False
# Create a directed graph with a cycle
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Check if the graph has a cycle
print(g.has_cycle())  # Output: True

# Create a directed acyclic graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

# Check if the graph has a cycle
print(g.has_cycle())  # Output: False
