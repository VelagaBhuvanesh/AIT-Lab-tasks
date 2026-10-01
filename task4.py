# Minimax Algorithm

def minimax(tree, depth, maximizing):

    # Base case: Leaf node
    if isinstance(tree, int):
        return tree

    if maximizing:
        best = float('-inf')

        for child in tree:
            value = minimax(child, depth + 1, False)
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for child in tree:
            value = minimax(child, depth + 1, True)
            best = min(best, value)

        return best


# Game tree
game_tree = [
    [3, 5, 6],
    [9, 1, 2],
    [0, -1, 4]
]

print("MINIMAX ALGORITHM")
print("-----------------")

print("Game Tree:", game_tree)

optimal_value = minimax(game_tree, 0, True)

print("Optimal Value:", optimal_value)
print("Best Move: First Branch")