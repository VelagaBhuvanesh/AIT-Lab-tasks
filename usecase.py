
import math
import heapq
import matplotlib.pyplot as plt

# Locations and their map coordinates (x, y)
locations = {
    "Central Station": (0, 0),
    "City Hospital": (2, 3),
    "University": (4, 5),
    "Tech Park": (7, 5),
    "Shopping Mall": (5, 2),
    "Airport": (10, 3),
    "Bus Terminal": (3, -2),
    "Museum": (7, 0)
}

# Road connections between locations
roads = [
    ("Central Station", "City Hospital"),
    ("Central Station", "Bus Terminal"),
    ("Central Station", "Shopping Mall"),
    ("City Hospital", "University"),
    ("City Hospital", "Shopping Mall"),
    ("University", "Tech Park"),
    ("University", "Shopping Mall"),
    ("Shopping Mall", "Bus Terminal"),
    ("Shopping Mall", "Museum"),
    ("Tech Park", "Museum"),
    ("Tech Park", "Airport"),
    ("Museum", "Airport")
]

# Build a weighted graph using road distances
graph = {node: {} for node in locations}
ROAD_FACTOR = 1.15

def distance(a, b):
    x1, y1 = locations[a]
    x2, y2 = locations[b]
    return math.hypot(x2 - x1, y2 - y1)

for a, b in roads:
    cost = distance(a, b) * ROAD_FACTOR
    graph[a][b] = cost
    graph[b][a] = cost

# Heuristic: straight-line distance to destination
def heuristic(node, goal):
    return distance(node, goal) * ROAD_FACTOR

# A* search algorithm
def a_star(start, goal):
    queue = [(heuristic(start, goal), 0, start)]
    parent = {start: None}
    g_cost = {start: 0}
    visited = set()

    while queue:
        f, cost, current = heapq.heappop(queue)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], g_cost[goal], len(visited)

        for neighbor, weight in graph[current].items():
            new_cost = g_cost[current] + weight

            if new_cost < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_cost
                parent[neighbor] = current
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(
                    queue, (priority, new_cost, neighbor)
                )

    return None, float("inf"), len(visited)

# Display the map and selected route
def show_map(path, start, goal):
    plt.figure(figsize=(10, 6))

    for a, b in roads:
        x1, y1 = locations[a]
        x2, y2 = locations[b]
        plt.plot([x1, x2], [y1, y2], "gray",
                 linewidth=1.5, zorder=1)

    for name, (x, y) in locations.items():
        plt.scatter(x, y, color="steelblue", s=90, zorder=3)
        plt.text(x + 0.12, y + 0.12, name, fontsize=8)

    if path:
        for a, b in zip(path, path[1:]):
            x1, y1 = locations[a]
            x2, y2 = locations[b]
            plt.plot([x1, x2], [y1, y2], "r-",
                     linewidth=4, zorder=2)

    sx, sy = locations[start]
    gx, gy = locations[goal]
    plt.scatter(sx, sy, color="green", s=180,
                label="Start", zorder=4)
    plt.scatter(gx, gy, color="red", s=180,
                label="Destination", zorder=4)

    plt.title("A* Heuristic-Based Map Navigation")
    plt.xlabel("Map X-coordinate")
    plt.ylabel("Map Y-coordinate")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main program
print("AVAILABLE LOCATIONS")
for name in locations:
    print("-", name)

start = input("\nEnter starting location: ").strip().title()
goal = input("Enter destination: ").strip().title()

# Match input against actual location names
lookup = {name.lower(): name for name in locations}
start = lookup.get(start.lower())
goal = lookup.get(goal.lower())

if not start or not goal:
    print("Invalid location. Please run again and use a listed name.")
elif start == goal:
    print("You are already at your destination!")
else:
    path, total_distance, expanded = a_star(start, goal)

    if path:
        print("\nOPTIMAL ROUTE FOUND")
        print(" -> ".join(path))
        print(f"Total distance: {total_distance:.2f} map units")
        print(f"Nodes expanded: {expanded}")
        print("Algorithm: A* Search")
        show_map(path, start, goal)
    else:
        print("No route exists between these locations.")
