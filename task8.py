# N-Queen Problem using Backtracking

N = 4
board = [-1] * N
solutions = []

# Check whether a position is safe
def is_safe(row, col):

    for i in range(row):

        # Check same column
        if board[i] == col:
            return False

        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve(row):

    # All queens are placed
    if row == N:
        solutions.append(board.copy())
        return

    # Try every column
    for col in range(N):

        if is_safe(row, col):

            board[row] = col

            solve(row + 1)

            # Backtrack
            board[row] = -1


# Display chessboard
def display(solution):

    for row in range(N):
        for col in range(N):
            if solution[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
print("4-QUEEN PROBLEM")
print("----------------")

solve(0)

for i, solution in enumerate(solutions, 1):

    print("\nSolution", i)
    display(solution)

print("\nTotal Solutions:", len(solutions))