a = input()
b = input()

result = int(a) * (int(b[-1]) + int(b[1]) * 10 + int(b[0]) * 100)

print(int(a) * int(b[-1]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(result)
