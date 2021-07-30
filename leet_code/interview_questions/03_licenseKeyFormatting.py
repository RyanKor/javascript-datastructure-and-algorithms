class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # condition : alphabet + number + dash
        s = ''.join(s.split("-"))
        cnt = len(s)
        answer = []
        if len(s) == 1:
            return s.upper()

        if len(s) % k != 0:
            answer.append(s[:len(s) % k] + "-")
            s = s[len(s) % k:]

        dash_cnt = (len(s) // k)
        while dash_cnt != 0:
            answer.append(s[:k])
            s = s[k:]
            dash_cnt -= 1
        if cnt % k != 0:
            s = answer[0] + '-'.join(answer[1:])
        else:
            s = '-'.join(answer)
        return s.upper()