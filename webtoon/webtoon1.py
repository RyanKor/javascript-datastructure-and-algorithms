def solution(S, pattern):
    answer = 0
    pattern = list(pattern)
    pattern.sort()
    pattern = ''.join(pattern)
    # pattern.sort()
    for i in range(len(S)):
        for j in range(len(pattern),len(S)+1):
            temp = list(S[i:j])
            temp.sort()
            temp = ''.join(temp)
            if pattern == temp:
                answer +=1
                break
    return answer

print(solution("tegsornamwaresomran", "ransom"))
print(solution("wreawerewa", "ware"	))