class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dic = {}
        if len(strs) == 1:
            return [strs]
        for i in strs:
            temp = ''.join(sorted(list(i)))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]

        for key, value in dic.items():
            value.sort()
            answer.append(value)
        answer.sort(key=lambda x : len(x))
        return answer