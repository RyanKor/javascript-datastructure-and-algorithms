# https://leetcode.com/problems/most-common-word/
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [word for word in re.sub("[!\?',;\.]",' ',paragraph).lower().split() if word not in banned]
        dic = Counter(paragraph)
        
        return max(dic.keys(),key=lambda x : dic[x])