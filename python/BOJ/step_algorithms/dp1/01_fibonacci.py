'''
문제
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

1
2
3
4
5
6
7
8
9
10
11
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        print() 0;
    } else if (n == 1) {
        printf("1");
        print() 1;
    } else {
        print() fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

*문제 풀이시 주의사항*
- 0, 1이 각 각 호출되는 순서는 피보나치 수열의 패턴으로 증가하게 된다.
N : 0 1 2 3 4 5 6 7 (호출될 자연수)
0 : 1 0 1 1 2 3 5 8
1 : 0 1 1 2 3 5 8 13
'''
import sys

num = int(sys.stdin.readline())


def dynamic_fibonacci(n):
    zero_count = [1, 0, 1]
    one_count = [0, 1, 1]
    if n == 0:
        print(1, 0)  # 0은 1회, 1은 0회 호출
    if n == 1:
        print(0, 1)   # 0은 0회, 1은 1회 호출
    if n == 2:
        print(1, 1)

    if n > 2:
        for i in range(3, n+1):  # n 값까지 배열에 담아줘야하므로 범위는 n+1까지로 지정
            zero_count.append(zero_count[i-1] + zero_count[i-2])
            one_count.append(one_count[i-1]+one_count[i-2])
        print(zero_count[n], one_count[n])


for i in range(num):
    test_case = int(sys.stdin.readline())
    dynamic_fibonacci(test_case)
