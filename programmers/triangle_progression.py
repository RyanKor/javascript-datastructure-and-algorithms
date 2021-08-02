# 프로그래머스 삼각 수열 문제 풀이
def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    # 2
    for i in range(n):
        for j in range(i, n):
            #3
            #down
            if i % 3 == 0:
                x += 1

            #right
            elif i % 3 == 1:
                y += 1

            #up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            #4
            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer


# def solution(n):
#     answer = []
#     tri = [[0]*n for i in range(n)]
#     # 아래 쪽의 for 반복문이 삼각형 형태로 순회할 수는 없다.
#     # 따라서 2차원 행렬을 정사각형 형태로 만들고, 삼각형이 가지 않는 곳은 0으로 채워서 빈 공간이라는 것을 명시한다.
#     x, y = -1,0
#     cnt = 1
#     for i in range(n):
#         for j in range(i, n):

#             if i % 3 == 0:
#                 x +=1
#             elif i % 3 == 1:
#                 y +=1
#             else:
#                 x-=1
#                 y-=1

#             tri[x][y] = cnt
#             cnt +=1
#     for i in tri:
#         for j in i:
#             if j != 0:
#                 answer.append(j)
#     return answer