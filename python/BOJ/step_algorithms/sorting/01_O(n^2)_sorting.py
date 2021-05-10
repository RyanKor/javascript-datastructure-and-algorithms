num = int(input())
temp = []
for i in range(num):
    temp.append(int(input()))

temp.sort()
for j in range(len(temp)):
    print(temp[j])
