'''
첫번째 이항계수 문제와 차이점이라면,

1) N의 범위가 늘었다 -> 1000
2) 재귀 함수로 문제를 풀기에 수가 너무 커졌다 -> 1000!

그리고 블로그들의 글을 읽어보면 이항계수 문제는 파스칼의 삼각형을 알고리즘 형태로 푸는 것과

비슷하다는 글이 많은데, 파스칼의 삼각형을 알고리즘으로 풀어보는 시도도 필요한 것 같다.
'''

n, k = map(int, input().split())
dp = [[0] * 1 for i in range(1001)]
dp[1].append(1)
for i in range(2, 1001):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
print(dp[n + 1][k + 1] % 10007)
