from collections import deque

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Breadth First Search
def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(path + [neighbor])

    return None


# Depth First Search
def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None


# Main program
print("GRAPH SEARCH ALGORITHMS")
print("-----------------------")

start = input("Enter start node (A-H): ").upper()
goal = input("Enter goal node (A-H): ").upper()

if start not in graph or goal not in graph:
    print("Invalid node! Please enter nodes from A to H.")
else:
    print("\nBFS Path:", bfs(start, goal))
    print("DFS Path:", dfs(start, goal))