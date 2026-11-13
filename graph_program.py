# Assessment 3.3 - Graph with BFS and DFS (default: last name MANGUMPIT)
from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}                      # adjacency list

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, u, v):              # undirected edge
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        """Breadth-first search using a queue and a visited set."""
        visited = {start}
        q = deque([start])
        order = []
        while q:
            v = q.popleft()
            order.append(v)
            for w in self.adj[v]:
                if w not in visited:
                    visited.add(w)
                    q.append(w)
        return order

    def dfs(self, start):
        """Depth-first search using recursion (the call stack) and a visited set."""
        visited, order = set(), []

        def visit(v):
            visited.add(v)
            order.append(v)
            for w in self.adj[v]:
                if w not in visited:
                    visit(w)

        visit(start)
        return order

    def show(self):
        for v, neighbors in self.adj.items():
            print(f"  {v:<2}: {', '.join(neighbors)}")


def default_graph():
    """Graph for MANGUMPIT: tree edges plus U-M2 and I-T (these make cycles)."""
    g = Graph()
    edges = [("M1", "A"), ("M1", "N"), ("A", "G"), ("A", "U"),
             ("N", "M2"), ("N", "P"), ("G", "I"), ("G", "T"),
             ("U", "M2"), ("I", "T")]
    for u, v in edges:
        g.add_edge(u, v)
    return g


def read_graph():
    """Let the user type their own edges, e.g.  A-B"""
    g = Graph()
    print("Enter edges like A-B (one per line). Press Enter on an empty line to finish.")
    while True:
        line = input("edge: ").strip().upper()
        if not line:
            break
        if "-" not in line:
            print("  Use the form A-B")
            continue
        u, v = [p.strip() for p in line.split("-", 1)]
        g.add_edge(u, v)
    return g


def main():
    choice = input("Use the MANGUMPIT graph? (Y/n): ").strip().lower()
    g = default_graph() if choice in ("", "y", "yes") else read_graph()
    if not g.adj:
        print("The graph is empty.")
        return

    print("\nAdjacency list:")
    g.show()

    first = next(iter(g.adj))
    start = input(f"\nStart vertex (press Enter for {first}): ").strip().upper() or first
    if start not in g.adj:
        print("That vertex is not in the graph.")
        return

    print("\n--- BFS (uses a queue) ---")
    print(", ".join(g.bfs(start)))
    print("\n--- DFS (uses a stack / recursion) ---")
    print(", ".join(g.dfs(start)))


if __name__ == "__main__":
    main()
