# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = Counter(stones)
        answer = 0
        for i in jewels:
            if i in cnt:
                answer += cnt[i]
        return answer
