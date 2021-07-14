def solution(s):
    answer = 0
    string = ["zero", "one","two", "three", "four","five", "six","seven","eight","nine"]
    dic = {}
    for i in range(10):
        dic[string[i]] = str(i)
    for i in string:
        if i in s:
            s = s.replace(i,dic[i])
    return int(s)