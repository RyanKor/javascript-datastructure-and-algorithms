# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        temp = dict(Counter(t))
        count = len(temp)

        i, j = 0, 0
        start = ""
        mini = 10 ** 6

        while j < len(s):

            if s[j] in temp:
                temp[s[j]] -= 1
                if temp[s[j]] == 0:
                    count -= 1

            while count == 0 and i <= j:

                if (j - i + 1) < mini:
                    mini = (j - i + 1)
                    start = s[i: j + 1]

                if s[i] in temp:
                    temp[s[i]] += 1
                    if temp[s[i]] == 1:
                        count += 1

                i += 1
            j += 1

        return start