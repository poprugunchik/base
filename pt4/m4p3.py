from collections import deque
n = int(input('Введите начало пути, от 1 до 8: '))

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5, 6],
    4: [7],
    5: [6, 7],
    6: [8],
    7: [8],
    8: []
}


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

bfs(graph, n)

