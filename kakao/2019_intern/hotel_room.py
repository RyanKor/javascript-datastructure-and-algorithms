def solution(k, room_number):
    answer = []

    # 정확도 테스트 통과, but 효율성 테스트 탈락
    # temp = [i for i in range(1,k+1)]
    # i = 0
    # while i < len(room_number):
    #     if room_number[i] in temp:
    #         answer.append(room_number[i])
    #         temp[temp.index(room_number[i])] = 0
    #         room_number[i] = 0
    #     else:
    #         for j in range(room_number[i]-1, len(temp)):
    #             if temp[j] != 0:
    #                 answer.append(temp[j])
    #                 temp[temp.index(temp[j])] = 0
    #                 room_number[i] = 0
    #                 break              
    #     i +=1
    
    # 방법 2 : 0 과 1을 활용한다.
    # https://jinomadstory.tistory.com/123
    dic = {}
    for i in room_number:
        n = i
        visit = [n]
        # print(visit)
        while n in dic: # 이미 지나온 경로 탐색하기
            n = dic[n]
            visit.append(n)
            print(dic)
            print(visit)
        answer.append(n)
        for j in visit:
            dic[j] = n +1
    return answer

print(solution(10, [1,3,4,1,3,1]))