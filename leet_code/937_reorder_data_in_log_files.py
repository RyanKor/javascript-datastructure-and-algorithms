# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_lst = []
        let_lst = []
        
        for i in logs:
            if ''.join(i.split()[1:]).isnumeric():
                num_lst.append(i)
            else:
                let_lst.append(i)
        
        let_lst.sort(key=lambda x : (x.split()[1:], x.split()[0]))

        return let_lst + num_lst