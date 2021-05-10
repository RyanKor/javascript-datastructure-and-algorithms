import sys

n = int(sys.stdin.readline())
string_case = sys.stdin.readline()
result = 0
for i in range(n):
    result += int(string_case[i])

print(result)
