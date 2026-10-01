import heapq

# Graph representing hospital road network
graph = {
    'Ambulance': {'Junction A': 4, 'Junction B': 6},
    'Junction A': {'Ambulance': 4, 'Junction C': 3, 'Junction D': 5},
    'Junction B': {'Ambulance': 6, 'Junction D': 2, 'Junction E': 4},
    'Junction C': {'Junction A': 3, 'Hospital': 5},
    'Junction D': {'Junction A': 5, 'Junction B': 2, 'Hospital': 4},
    'Junction E': {'Junction B': 4, 'Hospital': 3},
    'Hospital': {}
}

# Heuristic distances to hospital
heuristic = {
    'Ambulance': 10,
    'Junction A': 7,
    'Junction B': 5,
    'Junction C': 4,
    'Junction D': 3,
    'Junction E': 2,
    'Hospital': 0
}

# A* search algorithm
def astar(start, goal):

    open_list = [(heuristic[start], 0, start)]
    parent = {}
    g_cost = {start: 0}

    while open_list:

        f, cost, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path, cost

        if cost > g_cost[current]:
            continue

        for neighbor, distance in graph[current].items():

            new_cost = cost + distance

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (f_cost, new_cost, neighbor)
                )

    return None, float('inf')


# Main program
print("AMBULANCE ROUTE PLANNING USING A*")
print("----------------------------------")

start = 'Ambulance'
goal = 'Hospital'

path, distance = astar(start, goal)

if path:
    print("Starting Location:", start)
    print("Destination:", goal)
    print("Optimal Route:", " -> ".join(path))
    print("Total Distance:", distance, "km")
else:
    print("No route found!")