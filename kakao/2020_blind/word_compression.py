# https://programmers.co.kr/learn/courses/30/lessons/60057
# 테스트 케이스 갯수가 1000개 이하 -> 완전탐색이라 시간 복잡도를 크게 고려할 필요는 없었던 문제다.

# 방법 1 : 최소 길이 값을 min함수를 사용해 비교하며 완전 탐색
def solution(s):
    answer = len(s) # 값 비교를 위해 최대 배열 길이 지정
    result = ''
    for i in range(1, len(s)//2 + 1):
        cnt = 1
        temp = s[:i] # 최소 한 개
        for j in range(i, len(s), i): # 이 부분이 내가 잘 못떠올렸던 부분 -> 구간을 지정하면, 일정 간격으로 loop를 돌아야했다.
            if s[j:j+i] == temp:
                cnt +=1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + temp
                temp = s[j:j+i]
                cnt = 1
        if cnt == 1:
            cnt = ''
        result += str(cnt) + temp
        answer = min(answer, len(result))
        result = ''
    return answer




print(solution("abcabcabcabcdededededede"))