def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for adjacent in graph.get(node, []):  # Use .get() to avoid KeyError
            dfs(visited, graph, adjacent)

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend([adj for adj in graph.get(node, []) if adj not in visited])

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node = input("Enter the node: ").strip()
        adjacents = input(f"Enter the adjacents of {node} (space-separated): ").split()
        graph[node] = adjacents
    return graph

# Driver Code
print("Enter the graph details:")
graph = input_graph()
start_node = input("Enter the starting node: ").strip()

while True:
    print("\nChoose the traversal method:")
    print("1. DFS (Depth-First Search)")
    print("2. BFS (Breadth-First Search)")
    print("3. Exit")
   
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        print("\nFollowing is the Depth-First Search:")
        dfs(set(), graph, start_node)  # Pass a fresh set
    elif choice == '2':
        print("\nFollowing is the Breadth-First Search:")
        bfs(graph, start_node)  # No need to pass `visited` separately
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again!")

