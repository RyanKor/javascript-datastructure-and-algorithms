
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42889#
# 첫번째 솔루션 --> 시간 초과
# def solution(N, stages):
#     answer = []
#     length = len(stages)
#     temp = {}
#     result = {}
#     compare = {}
#     # 각 스테이지별 클리어 못한 인원을 카운트
#     for i in stages:
#         if i == N +1:
#             temp[int(i)] = 0
#         else:
#             temp[int(i)] = stages.count(i)
#     temp = dict(sorted(temp.items(), key=lambda x : x[0]))
#     for i in range(1,N+1):
#         if i in temp:
#             result[i] = temp[i]
#         else:
#             result[i] = 0
#     for key, value in temp.items():
#         # string = str(value) + "/" + str(length)
#         compare[key] = value / length
#         length = length - value
#     for key, value in compare.items():
#         if key in result:
#             result[key] = value
#         else:
#             pass
#     result = dict(sorted(result.items(), key=lambda x : x[1], reverse=True))
#     for key, value in result.items():
#         answer.append(key)
#     return answer

def solution(N, stages):
    answer = []
    length = len(stages)
    result = {}
    for i in range(1,N+1):
        if length !=0:
            cnt = stages.count(i)
            result[i] = cnt / length
            length = length - cnt
        else:
            result[i] = 0
    answer = sorted(result, key=lambda x : result[x], reverse=True)
    return answer