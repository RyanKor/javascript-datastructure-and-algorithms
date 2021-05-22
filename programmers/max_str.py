
# 첫번째 풀이 -> 시간 초과
# from itertools import permutations
# def solution(numbers):
#     answer = ''
#     comb = list(permutations(map(str,numbers),len(numbers)))
#     lst = []
#     for i in comb:
#         temp = ''.join(i)
#         lst.append(temp)
#     answer = max(lst)
#     return answer
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    # x*3 의 의미 : 숫자 제한 사항이 1000까지므로 자리수를 맞춰주는 과정
    return str(int(''.join(numbers)))
print(solution([6, 10, 2]))