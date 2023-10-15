from collections import deque

# Graph representation as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            queue.extend(graph[node])

    return result

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            result.append(node)
            visited.add(node)
            stack.extend(graph[node][::-1])  # Reverse to maintain alphabetical order

    return result

# Applying BFS and DFS
start_node = 'A'
bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

print("BFS:", bfs_result)
print("DFS:", dfs_result)
