import random

# Locations in the ride-sharing network
locations = [
    "Driver",
    "Pickup A",
    "Pickup B",
    "Pickup C",
    "Drop A",
    "Drop B",
    "Drop C"
]

# Distance matrix
distance = [
    [0, 4, 6, 8, 7, 9, 10],
    [4, 0, 3, 6, 5, 8, 9],
    [6, 3, 0, 4, 6, 5, 8],
    [8, 6, 4, 0, 3, 4, 6],
    [7, 5, 6, 3, 0, 3, 5],
    [9, 8, 5, 4, 3, 0, 2],
    [10, 9, 8, 6, 5, 2, 0]
]

# ACO parameters
NUM_ANTS = 10
ITERATIONS = 50
ALPHA = 1
BETA = 2
EVAPORATION = 0.5
Q = 100

N = len(locations)

# Initialize pheromone matrix
pheromone = [[1.0 for _ in range(N)] for _ in range(N)]

# Calculate route distance
def route_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    return total


# Select next location
def select_next(current, unvisited):
    probabilities = []

    for city in unvisited:
        tau = pheromone[current][city] ** ALPHA
        eta = (1 / distance[current][city]) ** BETA
        probabilities.append(tau * eta)

    total = sum(probabilities)

    probabilities = [p / total for p in probabilities]

    return random.choices(
        unvisited,
        weights=probabilities,
        k=1
    )[0]


# Ant Colony Optimization
def ant_colony():

    global pheromone

    best_route = None
    best_distance = float("inf")

    for iteration in range(ITERATIONS):

        all_routes = []

        for ant in range(NUM_ANTS):

            route = [0]
            unvisited = list(range(1, N))

            while unvisited:

                current = route[-1]
                next_city = select_next(current, unvisited)

                route.append(next_city)
                unvisited.remove(next_city)

            route.append(0)

            total = route_distance(route)

            all_routes.append((route, total))

            if total < best_distance:
                best_distance = total
                best_route = route

        # Pheromone evaporation
        for i in range(N):
            for j in range(N):
                pheromone[i][j] *= (1 - EVAPORATION)

        # Pheromone deposition
        for route, total in all_routes:

            deposit = Q / total

            for i in range(len(route) - 1):
                a = route[i]
                b = route[i + 1]

                pheromone[a][b] += deposit
                pheromone[b][a] += deposit

    return best_route, best_distance


# Main program
print("RIDE-SHARING TRIP OPTIMIZATION")
print("--------------------------------")

best_route, best_distance = ant_colony()

print("\nOptimal Route:")

for location in best_route:
    print(locations[location], end=" -> ")

print("\n\nTotal Travel Distance:", best_distance, "km")