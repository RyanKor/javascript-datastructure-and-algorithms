from itertools import product


def solution(word):
    answer = 0
    dic = {}
    answer = []
    vowel = ["A", "E", "I", "O", "U"]
    for i in vowel:
        answer.append(i)
    second = list(product(vowel, repeat=2))
    for i in second:
        temp = ''.join(i)
        answer.append(temp)
    third = list(product(vowel, repeat=3))
    for i in third:
        temp = ''.join(i)
        answer.append(temp)
    fourth = list(product(vowel, repeat=4))
    for i in fourth:
        temp = ''.join(i)
        answer.append(temp)
    fivth = list(product(vowel, repeat=5))
    for i in fivth:
        temp = ''.join(i)
        answer.append(temp)

    ################################

    return answer  #(len(vowel), len(second), len(third), len(fourth), len(fivth))


print(solution("AAAAE"))