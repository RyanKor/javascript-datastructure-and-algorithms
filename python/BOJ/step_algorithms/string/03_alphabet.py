import sys
alphabet = sys.stdin.readline().rstrip()

result = [-1] * 26
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for word in range(len(alphabet)):
    if result[english.index(alphabet[word])] == -1:
        result[english.index(alphabet[word])] = word

for i in result:
    print(i, end=" ")
