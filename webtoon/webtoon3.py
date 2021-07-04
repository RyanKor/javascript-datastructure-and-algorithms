def solution(letters, k):
    answer = ''
    temp = sorted(letters)[::-1]
    temp = temp[:k]
    for i in letters:
        if i not in temp:
            letters = letters.replace(i, "")
    return letters


print(solution("zbgaj", 3))
print(solution("qwerasdfzxcv", 5))
print(solution("zayokmb", 4))
print(solution("qwklefhakjdfhaksjdhfkljqwheflkqwfasdkfljwertyoip", 20))