import heapq

def prim_mst(graph, num_nodes):
    visited = [False] * num_nodes
    min_heap = [(0, 0)]  # (cost, start_node)
    mst_cost = 0
    mst_edges = []
    parent = [-1] * num_nodes
    
    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        
        visited[u] = True
        mst_cost += cost
        if parent[u] != -1:
            mst_edges.append((parent[u], u, cost))
        
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
                parent[v] = u
    
    return mst_cost, mst_edges

# User input for the graph
num_nodes = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(num_nodes)}
num_edges = int(input("Enter number of edges: "))

print("Enter edges in the format: node1 node2 weight")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

mst_cost, mst_edges = prim_mst(graph, num_nodes)

print("Minimum Spanning Tree Cost:", mst_cost)
print("Edges in MST:")
for edge in mst_edges:
    print(edge[0], "-", edge[1], "with cost", edge[2])
