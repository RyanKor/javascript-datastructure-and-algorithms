# 프로그래머스 단어 변환

result = list()


def solution(begin, target, words):
    global result
    answer = 0
    if target not in words:
        return 0
    elif target == begin:
        return 0

    visited = [False] * len(words)
    dfs(begin, target, words, visited, answer)
    return min(result)


def dfs(begin, target, words, visited, answer):
    global result
    if begin == target:
        return result.append(answer)

    change = list()

    for word in words:  #바꿀수 있는 단어 찾기
        count = 0
        for i in range(len(word)):
            if begin[i] != word[i]:
                count += 1
        if count == 1:
            change.append(word)

    for word in change:
        if not visited[words.index(word)]:  #방문한 단어가 아니면
            visited[words.index(word)] = True  #방문처리
            dfs(word, target, words, visited, answer + 1)  #재귀
            visited[words.index(word)] = False  #방문처리한거 되돌리기
