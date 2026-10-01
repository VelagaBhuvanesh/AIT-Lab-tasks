# Monkey Banana Problem using Goal Stack Planning

# Initial State
monkey = "door"
box = "window"
banana = "middle"
monkey_on_box = False
has_banana = False

# Goal Stack
goal_stack = ["has_banana"]

# Action sequence
actions = []

print("MONKEY BANANA PROBLEM")
print("---------------------")

print("\nInitial State:")
print("Monkey Position:", monkey)
print("Box Position:", box)
print("Banana Position:", banana)

# Goal Stack Planning
while goal_stack:

    goal = goal_stack.pop()

    if goal == "has_banana":

        if has_banana:
            continue

        if monkey != box:
            goal_stack.append("has_banana")
            goal_stack.append("move_to_box")

        elif box != banana:
            goal_stack.append("has_banana")
            goal_stack.append("push_box")

        elif not monkey_on_box:
            goal_stack.append("has_banana")
            goal_stack.append("climb_box")

        else:
            goal_stack.append("grasp_banana")

    elif goal == "move_to_box":

        monkey = box
        actions.append("Monkey moves to the box")
        print("\nAction: Monkey moves to the box")

    elif goal == "push_box":

        box = banana
        monkey = banana
        actions.append("Monkey pushes the box beneath the bananas")
        print("Action: Monkey pushes the box beneath the bananas")

    elif goal == "climb_box":

        monkey_on_box = True
        actions.append("Monkey climbs onto the box")
        print("Action: Monkey climbs onto the box")

    elif goal == "grasp_banana":

        has_banana = True
        actions.append("Monkey grasps the bananas")
        print("Action: Monkey grasps the bananas")

# Final State
print("\nFinal State:")
print("Monkey Position:", monkey)
print("Box Position:", box)
print("Monkey on Box:", monkey_on_box)
print("Has Banana:", has_banana)

print("\nPlan Executed:")
for i, action in enumerate(actions, 1):
    print(i, action)

if has_banana:
    print("\nGoal Achieved Successfully!")
else:
    print("\nGoal Not Achieved!")