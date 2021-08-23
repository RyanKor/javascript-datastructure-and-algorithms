# https://programmers.co.kr/learn/courses/30/lessons/84325/solution_groups?language=python3

def solution(table, languages, preference):
    answer = {}
    score = [0,5,4,3,2,1] # 직군별 언어 점수
    result = [] # 최대값이 여러개일 때, 결과 값을 리스트에 삽입하고 정렬 후, 사전순 정렬 후 첫번째 값 반환
    for td in table:
        td = td.split() # 문자열을 띄어쓰기 기준으로 분할 후, 리스트 요소에 따른 연산 수행
        answer[td[0]] = 0 # 딕셔너리 초기화
        for i in range(len(languages)): # 1 ≤ languages의 길이 ≤ 9
        #     answer[td[0]].append(score[td.index(languages[i])] * preference[i])
            if languages[i] not in td:
                answer[td[0]] +=score[0] * preference[i]
            else:
                answer[td[0]] += score[td.index(languages[i])] * preference[i]
    for k,v in answer.items():
        if max(answer.values()) == v:
            result.append(k)
    return sorted(result)[0]