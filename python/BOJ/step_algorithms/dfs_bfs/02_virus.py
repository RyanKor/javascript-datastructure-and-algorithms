import sys

computer = int(sys.stdin.readline())
net_pair = int(sys.stdin.readline())
dic={}
for i in range(computer):
    dic[i+1] = set()
for j in range(net_pair):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)
print(dic)