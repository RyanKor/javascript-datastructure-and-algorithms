'''
문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
'''
import sys

test = list(sys.stdin.readline().rstrip())
for i in range(len(test)):
    for j in range(i+1, len(test)):
        if int(test[i]) > int(test[j]):
            test[i], test[j] = test[j], test[i]
print(''.join(test[::-1]))
