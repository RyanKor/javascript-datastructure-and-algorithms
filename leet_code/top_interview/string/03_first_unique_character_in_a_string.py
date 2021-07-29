# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for idx, word in enumerate(s):
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        for key, value in dic.items():
            if value == 1:
                return s.index(key)

        return -1