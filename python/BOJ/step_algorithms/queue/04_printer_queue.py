# https://www.acmicpc.net/problem/1966
from collections import deque 
t = int(input()) 
for _ in range(t):
    n , target = map(int,input().split()) # n, m
    que = deque(list(map(int,input().split()))) # 문서 중요도
    idx_que = deque(list(range(n))) # 문서 인덱스
    cnt = 0 
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft() # 줄력한다.
            if idx_que.popleft() == target: # 출력한 문서가 찾고자하는 타겟 값이라면
                print(cnt) # 몇 번째로 출력되었는지 프린트로 결과를 보여준다.
        else:
            que.append(que.popleft()) # 출력할 중요도 순서가 아니므로 뒤로 미룬다.
            idx_que.append(idx_que.popleft()) # 마찬가지로 문서도 뒤로 미룬다.