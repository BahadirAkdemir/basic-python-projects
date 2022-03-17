graph = {
    'A': ['D', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': [],
    'F': ['C']
}

#Graph is like:

#               A
#             /   \
#            D     C
#           /     / \
#          B     A   F
#        / | \  ...   \
#       A  D  E         C
#      ... ...          ...

# Algorithm should check with order A-D-C-B-F-E


queue = [] #order of nodes to visit
visited = [] #nodes already visited (to avoid cycles)

def bfs(graph, queue, visited, first_node):
    queue.append(first_node)
    visited.append(first_node)

    while queue:

        node = queue.pop(0)
        print(node)
        for neighbors in graph[node]:
            if neighbors not in visited:
                queue.append(neighbors)
                visited.append(neighbors)

print("BFS:")
bfs(graph, queue, visited, 'A')
