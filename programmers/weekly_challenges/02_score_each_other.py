# 문제명 : 상호 평가
def solution(scores):
    answer = ''
    scores[:] = list(zip(*scores)) # 배열 전치 형렬 진행
    
    for i in range(len(scores)):
        temp = [] # 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점인 경우 필터링
        avg = 0 # 평균 점수 초기화
        for j in range(len(scores)):
            if (i == j) and scores[i].count(scores[i][j]) == 1 and (scores[i][j] == max(scores[i]) or scores[i][j] == min(scores[i])):
                pass
            else:
                temp.append(scores[i][j])
        avg = sum(temp) / len(temp)
        if avg >= 90 : 
            answer += "A"
        elif 80 <= avg <90:
            answer += "B"
        elif 70 <= avg <80:
            answer += "C"
        elif 50 <= avg <70:
            answer += "D"
        else:
            answer += "F"
    return answer