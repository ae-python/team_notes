from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # iterate until the queue is empty.
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        # insert uninvited nodes to the queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

# BFS(graph, 1, visited)