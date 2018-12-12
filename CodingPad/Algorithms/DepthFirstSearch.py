# Implementation of the depth first seach algorithm for a graph


# dfs with initial empty visited array
def dfs(graph, start, visited=[]):
    # add the root in visited
    if start not in visited:
        visited.append(start)

    # for each adjacent node recurse as it being the start
    for n in graph[start]:
        if n not in visited:
            visited.append(n)
            visited = dfs(graph, n, visited)

    return visited


# main function
if __name__ == '__main__':
    print("depth first search")
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F', 'G']),
             'F': set(['C', 'E']),
             'G': set([])}

    # depth first search from A
    print(dfs(graph, 'A'))