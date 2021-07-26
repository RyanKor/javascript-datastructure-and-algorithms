# https://leetcode.com/problems/generate-parentheses/
from itertools import product


# solution1 : itertools를 사용한 풀이
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        p_set = []
        test = list(product(["(", ")"], repeat=n * 2))
        for i in test:
            temp = ''.join(i)
            if temp.count("(") == len(temp) // 2 and temp.count(
                    ")") == len(temp) // 2 and temp[0] != ")":
                p_set.append(temp)

        for i in p_set:
            stack = []
            for j in range(len(i)):
                if i[j] == "(":
                    stack.append(j)
                else:
                    if stack != []:
                        stack.pop()
                    else:
                        break

                if j == len(i) - 1 and stack == []:
                    answer.append(i)

        return answer


# solution2 : DFS 연산속도 상위 95%...;
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if not n:
#             return []
#         left, right, ans = n, n, []
#         self.dfs(left, right, ans, "")
#         return ans

#     def dfs(self, left, right, ans, string):
#         if right < left:
#             return
#         if not left and not right:
#             ans.append(string)
#             return
#         if left:
#             self.dfs(left - 1, right, ans, string + "(")
#         if right:
#             self.dfs(left, right - 1, ans, string + ")")
