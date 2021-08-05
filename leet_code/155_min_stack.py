# https://leetcode.com/problems/min-stack/

"""
    # original my solution : it's 10 times lower than the solution below.
    def __init__(self):
        '''
        initialize your data structure here.
        '''
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
"""

import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.Min = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.Min.append(min(sys.maxsize if len(self.Min)==0 else self.Min[-1], val))

    def pop(self) -> None:
        self.arr.pop()
        self.Min.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()