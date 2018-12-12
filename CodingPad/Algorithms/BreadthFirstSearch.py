# Implementation of breadth first search for a graph
from collections import deque

# uses queue to keep track of nodes in each level
def bfs(graph, start, visited=[]):
    q = deque()
    q.append(start)

    while not q.__len__() == 0:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                q.append(n)

    return visited


# main function
if __name__ == '__main__':
    print("breadth first search")
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F', 'G']),
             'F': set(['C', 'E']),
             'G': set([])}

    # breadth first search from A
    print(bfs(graph, 'A'))