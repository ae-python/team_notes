def DFS(graph, v, visited):
    # make current node visited.
    visited[v] = True
    print(v, end=' ')
    # visit adjacent node recursively.
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

# # adjacency matrix
# graph = [
#     [],         # for processing index
#     [2, 3, 8],  # adjacent nodes with node 1
#     [1, 7],     # node 2
#     [1, 4, 5],  # node 3
#     [3, 5],     # node 4
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]      # node 8
# ]

# # information of nodes visited
# visited = [False] * 9

# DFS(graph, 1, visited)