# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        open_paren = "([{"
        stack = []
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        for i in s:
            if i in open_paren:
                stack.append(i)
            else:
                if i == ")":
                    if stack != [] and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i == "]":
                    if stack != [] and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif i == "}":
                    if stack != [] and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if stack == []:
            return True

        return False