# Hill Climbing Algorithm

def hill_climbing(start, goal):
    current = start
    path = [current]

    # Heuristic function
    def heuristic(state):
        return abs(goal - state)

    print("Starting State:", current)

    while current != goal:

        # Generate neighboring states
        neighbors = [current - 1, current + 1]

        # Select the best neighbor
        next_state = min(
            neighbors,
            key=lambda x: heuristic(x)
        )

        # Check for improvement
        if heuristic(next_state) >= heuristic(current):
            print("Local Maximum or Stuck!")
            break

        current = next_state
        path.append(current)

        print("Current State:", current)

    print("\nFinal Path:", path)
    print("Total Steps:", len(path) - 1)

    if current == goal:
        print("Goal Reached Successfully!")
    else:
        print("Goal Not Reached!")


# Main Program
start = int(input("Enter starting state: "))
goal = int(input("Enter goal state: "))

hill_climbing(start, goal)