from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def dfs(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_path = self.dfs(neighbor, end, path)
                if new_path:
                    return new_path
        return None

    def bfs(self, start, end):
        queue = deque([(start, [start])])
        levels = {start: 0}  # Store levels of nodes
        while queue:
            current, path = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    levels[neighbor] = levels[current] + 1
                    if neighbor == end:
                        return new_path, levels  # Return both path and levels
                    else:
                        queue.append((neighbor, new_path))
        return None, None

    def display_level_order(self, levels):
        max_level = max(levels.values())
        print("\nLevel Order Traversal:")
        for level in range(max_level + 1):
            level_nodes = [node for node, level_value in levels.items() if level_value == level]
            print(f"Level {level}: {level_nodes}")

    def display_graph(self):
        print("\nCurrent State of the Graph:")
        for node, neighbors in self.graph.items():
            print(f"\nNode {node} Connects To: {neighbors}")

# User input for graph
network = Graph()
num_nodes = int(input("\nEnter the Number of Nodes in the Network: "))

for _ in range(num_nodes):
    node = int(input("Enter Node: "))
    network.add_node(node)

num_edges = int(input("\nEnter the Number of Edges in the Network: "))

print("\n")
for _ in range(num_edges):
    u, v = map(int, input("Enter Edge (u v): ").split())
    network.add_edge(u, v)

levels = None

while True:
    print("\nOptions:")
    print("1. Display Graph")
    print("2. Add Node")
    print("3. Network Routing using DFS")
    print("4. Network Routing using BFS")
    print("5. Display Level Order Traversal")
    print("6. Quit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        network.display_graph()

    elif choice == 2:
        new_node = int(input("\nEnter the New Node to Add: "))
        network.add_node(new_node)

    elif choice == 3:
        start_node = int(input("\nEnter the Start Node: "))
        end_node = int(input("Enter the End Node: "))
        if start_node in network.graph and end_node in network.graph:
            dfs_path = network.dfs(start_node, end_node)
            print(f"\nDFS Shortest Path from {start_node} to {end_node}: {dfs_path}")
        else:
            print("\nInvalid Start or End Node.")

    elif choice == 4:
        start_node = int(input("\nEnter the Start Node: "))
        end_node = int(input("Enter the End Node: "))
        if start_node in network.graph and end_node in network.graph:
            bfs_path, levels = network.bfs(start_node, end_node)
            print(f"\nBFS Shortest Path from {start_node} to {end_node}: {bfs_path}")
        else:
            print("\nInvalid Start or End Node.")

    elif choice == 5:
        if levels is not None:
            network.display_level_order(levels)
        else:
            print("\nPlease perform BFS first to calculate level order traversal.")

    elif choice == 6:
        print("\nExiting the Program...\n")
        break
    
    else:
        print("\nInvalid Choice. Please Enter a Valid Option.")