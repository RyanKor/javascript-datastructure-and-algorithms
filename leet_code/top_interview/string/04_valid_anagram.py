# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1
        # s,t = list(s), list(t)
        # s.sort()
        # t.sort()
        # if s == t:
        #     return True
        # return False

        # solution2
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in t:
            if i in dic:
                if dic[i] == 1:
                    dic.pop(i)
                else:
                    dic[i] -= 1
            else:
                return False
        if len(dic) == 0:
            return True

        return False