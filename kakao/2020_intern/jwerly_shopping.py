
# https://programmers.co.kr/learn/courses/30/lessons/67258
# from collections import deque
# # 첫번째 도전 --> 실패 / 이유 : 시간 초과 (효율성 판단이 들어가는 문제)
# def solution(gems):
#     answer = []
#     check = list(set(gems))
#     if len(check) == 1:
#         return [1,1]
#     check.sort()
#     for i in range(len(gems)):
#         for j in range(i+1,len(gems)+1):
#             temp = list(set(gems[i:j]))
#             temp.sort()
#             if check == temp:
#                 answer.append([i+1,j])
#                 break
#             else:
#                 pass
#     answer.sort(key=lambda x : abs(x[0]-x[1]))
#     return answer[0]


# 두번째 도전 --> 실패 / 이유 : 시간 초과 (정확도 테스트는 모두 통과, 그러나 효율성 테스트 12개 통과 못함)
# gems 배열 자체를 정렬하면 안된다.
# def solution(gems):
#     answer = []
#     check = list(set(gems))
#     i,j = 0, 0
#     mini = len(gems)
#     while j <= len(gems):
#         temp = list(set(gems[i:j]))
#         if len(check) > len(temp): # 범위 안의 보석의 갯수가 더 적은 경우
#             j +=1
#         else:
#             if len(check) == len(temp):
#                 mini = min(mini, len(temp))
#                 answer.append([i+1,j])
#             i +=1
#     answer.sort(key=lambda x : abs(x[0]-x[1]))
#     return answer[0]


# 세번째 도전 --> 실패 / 이유 : 시간 초과 (정확도 테스트는 모두 통과, 그러나 효율성 테스트 12개 통과 못함)
def solution(gems):
    answer = []
    check = list(set(gems))
    i,j = 0, 0
    mini = len(gems) + 1
    dic = {}
    while j < len(gems):
        if gems[j] not in dic: # 범위 안의 보석의 갯수가 더 적은 경우
            dic[gems[j]] = 1
        else:
            dic[gems[j]] += 1
        j +=1
        if len(check) == len(dic):
            while i < j: # start_p 가 end_p 보다 같을 때까지 증가
                if dic[gems[i]] > 1: # start_p에 해당하는 보석이 구간 내에 하나 이상 있다면
                    dic[gems[i]] -= 1 # 구간 내 보석 하나 감소(start_p 의 보석 뺄거니까)
                    i += 1 # start_p 증가
                    
                elif mini > j - i: # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
                    mini = j - i
                    answer = [i+1, j] # answer와 최단거리 갱신
                    break
                else:
                    break
    return answer