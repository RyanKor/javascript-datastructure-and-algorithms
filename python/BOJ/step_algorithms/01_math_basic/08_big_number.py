'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)

출력
첫째 줄에 A+B를 출력한다.

*주의 사항*

파이썬 같은 언어는 10,000자리 정도의 자연수도 자유롭게 다룰 수 있습니다. 
하지만 C/C++이라면 이 문제를 어떻게 풀까요? C/C++ 사용자가 아니더라도 고민해 보면 좋을 것입니다.

큰 수 표현에 대한 참고 자료
https://kamang-it.tistory.com/entry/AlgorithmBig-Integer%ED%81%B0%EC%88%98-%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0

C++을 배우고 나면, 반드시 이 문제는 다시 풀어보자.
'''
import sys
A, B = map(int, sys.stdin.readline().split())

print(A+B)
