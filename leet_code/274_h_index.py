# https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        answer = 0
        answer = max(map(min, enumerate(citations, start=1)))
        return answer