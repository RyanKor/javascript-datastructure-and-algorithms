# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = []
        
        for i in emails:
            i = i.split("@")
            i[0] = i[0].replace('.','')
            if '+' in i[0]:
                i[0] = i[0][:i[0].index('+')]
            
            temp = '@'.join(i)
            if temp not in answer:
                answer.append(temp)
            
        return len(answer)