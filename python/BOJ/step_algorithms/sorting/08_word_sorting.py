'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

def mergeSort(a):
    if len(a) > 1: # 배열의 길이가 1보다 클 경우 재귀함수 호출 반복
        mid = len(a)//2 # 2로 나눈 몫 (중간 값) 취함
        la, ra = a[:mid], a[mid:] # la 중간 값을 기준으로 왼쪽, ra 중간 값을 기준으로 오른쪽
        mergeSort(la) # 왼쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        mergeSort(ra) # 오른쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        li, ri, i = 0, 0, 0 # 정렬을 위한 변수 선언 (왼쪽, 오른쪽, 기준)
        while li < len(la) and ri < len(ra): # 서브 리스트의 정렬이 끝날 때까지 반복
            if la[li] < ra[ri]: # 오른쪽 리스트의 값이 클 경우라면
                a[i] = la[li] # 왼쪽 리스트의 해당 인덱스의 값을 할당
                li += 1 # 왼쪽 리스트의 인덱스 하나 증가
            else: # 왼쪽 리스트의 값이 클 경우라면
                a[i] = ra[ri] # 오른쪽 리스트의 해당 인덱스의 값을 할당
                ri += 1 # 오른쪽 리스트의 인덱스 하나 증가
            i += 1 # 기준 인덱스 증가
        a[i:] = la[li:] if li != len(la) else ra[ri:]
      # 왼쪽 리스트의 인덱스의 값이 서브 리스트의 값과 같지 않을 경우라면(정렬 끝),
      # 왼쪽 서브 리스트의 값을 리스트에 덮어쓰기, 그렇지 않은 경우라면 오른쪽 서브 리스트의 값 할당                                   
mergeSort(a)
'''
import sys

num = int(sys.stdin.readline().rstrip())

result = []
for i in range(num):
    words = sys.stdin.readline().rstrip()
    result.append(words)

result = list(set(result))


def mergeSort(a):
    if len(a) > 1:  # 배열의 길이가 1보다 클 경우 재귀함수 호출 반복
        mid = len(a)//2  # 2로 나눈 몫 (중간 값) 취함
        la, ra = a[:mid], a[mid:]  # la 중간 값을 기준으로 왼쪽, ra 중간 값을 기준으로 오른쪽
        mergeSort(la)  # 왼쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        mergeSort(ra)  # 오른쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        li, ri, i = 0, 0, 0  # 정렬을 위한 변수 선언 (왼쪽, 오른쪽, 기준)
        while li < len(la) and ri < len(ra):  # 서브 리스트의 정렬이 끝날 때까지 반복
            if len(la[li]) < len(ra[ri]):  # 오른쪽 리스트의 값이 클 경우라면
                a[i] = la[li]  # 왼쪽 리스트의 해당 인덱스의 값을 할당
                li += 1  # 왼쪽 리스트의 인덱스 하나 증가
            elif len(la[li]) == len(ra[ri]):
                if la[li] < ra[ri]:  # 오른쪽 리스트의 값이 클 경우라면
                    a[i] = la[li]  # 왼쪽 리스트의 해당 인덱스의 값을 할당
                    li += 1  # 왼쪽 리스트의 인덱스 하나 증가
                else:  # 왼쪽 리스트의 값이 클 경우라면
                    a[i] = ra[ri]  # 오른쪽 리스트의 해당 인덱스의 값을 할당
                    ri += 1  # 오른쪽 리스트의 인덱스 하나 증가
            else:  # 왼쪽 리스트의 값이 클 경우라면
                a[i] = ra[ri]  # 오른쪽 리스트의 해당 인덱스의 값을 할당
                ri += 1  # 오른쪽 리스트의 인덱스 하나 증가
            i += 1  # 기준 인덱스 증가
        a[i:] = la[li:] if li != len(la) else ra[ri:]
    return a


for i in mergeSort(result):
    print(i)
