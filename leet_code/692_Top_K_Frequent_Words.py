# https://leetcode.com/problems/top-k-frequent-words/


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        word = Counter(words)
        return [i[0] for i in word.most_common(k)]

