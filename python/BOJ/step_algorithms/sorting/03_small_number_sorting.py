'''
수의 범위가 작다면 카운팅 정렬(계수 정렬)을 사용하여 더욱 빠르게 정렬할 수 있습니다.

참고 자료
https://bowbowbow.tistory.com/8

방법상, sorted 내장 메소드를 사용하면 분명 메모리 초과가 발생한다.
평상시에 주어진 메모리가 256MB인데, 여기서는 8MB가 주어져서 극강의 메모리 효율을 보여줘야한다.
'''

import sys

case = int(sys.stdin.readline())
result = [0]*10001

# 가장 단순한 해결법 -> 메모리 초과
# for i in range(case):
#     num = int(sys.stdin.readline())
#     result.append(num)
# print(sorted(result))


# 두번째 해결법 : 딕셔너리 객체를 사용한 방법 -> 메모리 초과
# for i in range(case):
#     num = int(sys.stdin.readline())
#     if num in dic:
#         dic[num] += 1
#     else:
#         dic[num] = 1

# for key, value in sorted(dic.items(), key=lambda item: item[0]):
#     while value > 0:
#         result.append(key)
#         value -= 1

# for i in result:
#     print(i)

# 세번째 해결법 -> sorting을 쓰는 게 아니라 리스트와 인덱스를 활용해 풀어본다.
# 아니, 얘도 메모리 초과 뜨는데, 정답이 뭐지??
# for i in range(case):
#     num = int(sys.stdin.readline())
#     result[num] += 1

# cnt = 0
# while True:
#     if result[cnt] != 0:
#         print(cnt)
#         result[cnt] -= 1
#     else:
#         pass
#         cnt += 1
#     if cnt == len(result) - 1:
#         break

# 세번째 방법과 시도가 매우 유사한데, while을 사용하게되면, 여전히 메모리 초과를 벗어날 수 없다.
# while을 사용하는 상황을 매우 조심스럽게 생각해야하나;

for i in range(case):
    input_num = int(sys.stdin.readline())
    result[input_num] = result[input_num] + 1
for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)
