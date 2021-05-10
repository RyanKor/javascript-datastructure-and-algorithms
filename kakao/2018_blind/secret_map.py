# https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = bin(arr1[i] | arr2[i])[2:]
        if len(result) < n:
            result = '0'*(n-len(result))  + result
        text = ''
        for i in result:
            if i == '1':
                text += "#"
            else:
                text += " "
        answer.append(text)
    
    return answer