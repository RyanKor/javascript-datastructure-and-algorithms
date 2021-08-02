# 대부분의 경우 반복구현은 재귀로, 재귀는 반복구현으로 알고리즘 표현이 가능하기 때문에 익숙해질 때까지 자유롭게 풀어보자.
graph = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3]}


def dfs_recursive(graph, v, discovered):
    discovered.append(v)

    for edge in graph[v]:
        if edge not in discovered:
            discovered = dfs_recursive(graph, edge, discovered)

    return discovered


print(dfs_recursive(graph, 1, []))


def dfs_stack(graph, v):
    discovered = []
    stack = [v]

    while stack:
        top = stack.pop()

        if top not in discovered:
            discovered.append(top)
            for edge in graph[top]:
                stack.append(edge)
    return discovered


print(dfs_stack(graph, 1))