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

# Algorithm should check with order A-D-B-E-C-F


visited = [] #nodes already visited (to avoid cycles)

def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)
        print(node)
        for neighbors in graph[node]:
            dfs(graph, visited, neighbors)


print("DFS:")
dfs(graph, visited, 'A')
