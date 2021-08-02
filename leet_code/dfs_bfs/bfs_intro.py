from collections import deque
# BFS는 재귀로 구현이 불가능하기 때문에, 알고리즘 테스트 시 재귀로 구현하려는 삽질을 하지말자.
graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def bfs_queue(v, graph):
    queue = [v]
    discovered = [v]

    while queue:
        front = queue.pop(0)

        for edge in graph[front]:
            if edge not in discovered:
                discovered.append(edge)
                queue.append(edge)
    return discovered


print(bfs_queue(1, graph))


def bfs_deque(v, graph):
    queue = deque([v])
    discovered = [v]

    while queue:
        front = queue.popleft()
        for edge in graph[front]:
            if edge not in discovered:
                discovered.append(edge)
                queue.append(edge)
    return discovered


print(bfs_deque(1, graph))