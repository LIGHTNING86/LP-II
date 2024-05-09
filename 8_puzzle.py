import heapq
import itertools

# A* Node class to represent each state of the puzzle
class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state  # State of the puzzle (e.g., a tuple of numbers)
        self.parent = parent  # Parent node to track the solution path
        self.move = move  # The move that led to this state
        self.depth = depth  # Depth of the node (g-cost)
        self.goal = None  # Goal state, to be set later

    def __lt__(self, other):
        # Comparison operator for the priority queue
        return self.f() < other.f()

    def f(self):
        # f(n) = g(n) + h(n)
        return self.depth + self.heuristic()

    def heuristic(self):
        # Manhattan distance heuristic
        goal = self.goal
        distance = 0
        for idx, val in enumerate(self.state):
            if val == 0:
                continue
            goal_idx = goal.index(val)
            row1, col1 = divmod(idx, 3)
            row2, col2 = divmod(goal_idx, 3)
            distance += abs(row1 - row2) + abs(col1 - col2)
        return distance

    def is_goal(self):
        # Check if the state is the goal state
        return self.state == self.goal


# Function to generate possible moves
def possible_moves(state):
    index = state.index(0)  # Find the position of the empty tile
    row, col = divmod(index, 3)
    moves = []

    # Define the possible moves: up, down, left, right
    if row > 0:
        moves.append((index, index - 3))  # Move up
    if row < 2:
        moves.append((index, index + 3))  # Move down
    if col > 0:
        moves.append((index, index - 1))  # Move left
    if col < 2:
        moves.append((index, index + 1))  # Move right

    return moves


# Function to apply a move to a state
def apply_move(state, move):
    state_list = list(state)
    state_list[move[0]], state_list[move[1]] = state_list[move[1]], state_list[move[0]]
    return tuple(state_list)


# A* search algorithm to solve the puzzle, tracking all explored moves
def a_star_search(start_state, goal_state):
    open_list = []
    closed_set = set()
    explored_states = []  # List to store all explored states
    node_count = itertools.count()  # To ensure heap order when f() values are the same
    initial_node = Node(start_state)
    initial_node.goal = goal_state

    heapq.heappush(open_list, (initial_node.f(), next(node_count), initial_node))

    while open_list:
        _, _, current = heapq.heappop(open_list)

        # Display the current state with f(n), h(n), and g(n)
        print("Exploring state:")
        print_puzzle(current.state)
        print(f"f(n) = {current.f()}, h(n) = {current.heuristic()}, g(n) = {current.depth}")
        print()

        # Record this state in the explored list
        explored_states.append(current.state)

        if current.is_goal():
            # Goal reached, return the path and all explored states
            path = []
            while current:
                path.append((current.move, current.state))
                current = current.parent
            return path[::-1], explored_states  # Return reversed path and explored states

        closed_set.add(current.state)

        # Generate child nodes for each possible move
        for move in possible_moves(current.state):
            new_state = apply_move(current.state, move)

            if new_state in closed_set:
                continue  # Skip if the state is already explored

            new_node = Node(new_state, current, move, current.depth + 1)
            new_node.goal = goal_state

            heapq.heappush(open_list, (new_node.f(), next(node_count), new_node))

    return None, explored_states  # No solution found, but return all explored states


# Function to print a 3x3 puzzle grid with separators for a visual output
def print_puzzle(state):
    for i in range(3):
        row = ' | '.join(str(x) for x in state[i * 3:i * 3 + 3])
        print(row)
        if i < 2:
            print("---------")
    print()


# Function to read a 3x3 matrix from user input and convert it to a tuple
def read_puzzle():
    state = []
    for _ in range(3):
        row = list(map(int, input("Enter row (space-separated): ").split()))
        state.extend(row)
    return tuple(state)


# Main function to run the script
def main():
    # Read the start and goal states from user input
    print("\nEnter the puzzle START state (3x3 matrix):")
    start_state = read_puzzle()

    print("\nEnter the puzzle END/GOAL state (3x3 matrix):")
    goal_state = read_puzzle()

    # Find the solution using A* search
    solution, explored_states = a_star_search(start_state, goal_state)

    # Display all explored states as a list of numbers
    print("\nAll explored states (as lists):")
    for state in explored_states:
        print(list(state))

    # Display the solution path
    if solution:
        print("\nSOLUTION FOUND!\n")
        for step in solution:
            move, state = step
            print("Move:", move)
            print_puzzle(state)
    else:
        print("\nNO SOLUTION FOUND...\n")


# Run the main function
if __name__ == "__main__":
    main()
