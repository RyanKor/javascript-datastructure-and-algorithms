# https://leetcode.com/problems/permutations-ii/submissions/

from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # lst = list(permutations(nums, len(nums)))
        # solution1 : using set data type
        # # 생각보다 set을 사용한 연산법이 속도가 빠르지 않다. (정답은 맞다.)
        # # 더 빠른 연산에 대해 정답을 작성해 넣자.
        # lst = list(set(lst))
        # return lst

        # solution2 : DFS
        # 연산속도 상위 94%로 보임
        C = Counter(nums)
        B = []

        def dfs(arr):
            if not C:
                return B.append(list(arr))
            for k in list(C):
                arr.append(k)
                if C[k] == 1:
                    C.pop(k)  # delete key and return value
                else:
                    C[k] -= 1
                dfs(arr)
                arr.pop()
                C[k] += 1

        dfs([])
        return B