# Map Coloring using Constraint Satisfaction Problem

# Define regions and their neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store assigned colors
color_map = {}

# Check whether color is safe
def is_safe(region, color):
    for neighbor in graph[region]:
        if color_map.get(neighbor) == color:
            return False
    return True

# Backtracking function
def map_coloring(regions):

    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):

            color_map[region] = color

            if map_coloring(regions[1:]):
                return True

            del color_map[region]

    return False


# Main program
regions = list(graph.keys())

print("MAP COLORING USING CSP")
print("----------------------")

if map_coloring(regions):

    print("\nValid Coloring Solution:")

    for region, color in color_map.items():
        print(region, ":", color)

else:
    print("No valid coloring exists.")