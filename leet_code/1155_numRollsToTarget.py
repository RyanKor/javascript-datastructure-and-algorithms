# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dfs(d, path):
            res = 0
            if d < 0 or path > target:
                return 0

            if d == 0 and path == target:
                return 1

            if (d, path) in memo:
                return memo[(d, path)]

            for i in range(1, f + 1):
                res += dfs(d - 1, path + i)

            memo[(d, path)] = res

            return res

        return dfs(d, 0) % (10**9 + 7)
