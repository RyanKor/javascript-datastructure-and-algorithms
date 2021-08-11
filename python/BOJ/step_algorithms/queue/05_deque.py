# https://www.acmicpc.net/problem/10866

import sys
from collections import deque

num  =int(sys.stdin.readline().rstrip())

class Deque:
    def __init__(self):
        self.deq = deque([])
    
    def push_front(self, val):
        self.deq.appendleft(val)
    
    def push_back(self,val):
        self.deq.append(val)
    
    def pop_front(self):
        if len(self.deq) == 0:return -1
        return self.deq.popleft()
    
    def pop_back(self):
        if len(self.deq) == 0:return -1
        return self.deq.pop()

    def size(self):
        return len(self.deq)

    def empty(self):
        if len(self.deq) == 0:return 1
        return 0

    def front(self):
        if len(self.deq) == 0:return -1
        return self.deq[0]
    
    def back(self):
        if len(self.deq) == 0:return -1
        return self.deq[-1]

queue = Deque()

for i in range(num):
    cli = sys.stdin.readline().split()
    if cli[0] == "push_back":
        queue.push_back(int(cli[1]))
    
    elif cli[0] == "push_front":
        queue.push_front(int(cli[1]))
    
    elif cli[0] == "front":
        print(queue.front())
    
    elif cli[0] == "back":
        print(queue.back())

    elif cli[0] == "size":
        print(queue.size())
    
    elif cli[0] == "empty":
        print(queue.empty())

    elif cli[0] == "pop_front":
        print(queue.pop_front())

    elif cli[0] == "pop_back":
        print(queue.pop_back())