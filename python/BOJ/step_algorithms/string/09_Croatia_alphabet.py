'''
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=

크로아티아 문자열 문제 자체가 결국엔 여러개의 문자가 하나의 문자로 치환되는 것을 암시하기 때문에, replace를 사용해서

공백이 아닌 다른 한 개의 문자로 치환하는 과정을 보여주면 되지 않았나 싶다.
'''
import sys

test_case = sys.stdin.readline().rstrip()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for word in croatia_alphabet:
    test_case = test_case.replace(word, '#')


print(len(test_case))
