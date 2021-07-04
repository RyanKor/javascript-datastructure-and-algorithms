# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re, random

user_input = input()

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+")

# 로직 구성 방법 --> 1 ~ 7번 순서대로 구현하면 안맞는 로직이 있어 순서를 맞춰 진행할 필요는 없다.
# 1. 한글, 영어, 숫자 및 특수문자 ('.','_','/') 포함 정규식 작성
name = re.sub("[^ㄱ-ㅎ가-힣a-zA-Z0-9._/]", '',user_input)
print(name)
# 2. 이름의 길이는 2글자 이상, 20글자 미만
if len(name) == 1:
	ran_num = ''
	for i in range(4):
		ran_num += str(random.randint(0,9))
	name += ran_num
elif len(name) > 19:
	name = name[:19] # 20글자 이상인 부분부터 삭제해야함. (20 글자부터!) 즉, 0 ~ 18 까지!

# 4. 연속된 값 있을 경우 --> 통합
name = re.sub("[\.{2,}|\/{2,}|_{2,}]",'',name) # 3번 조건에서 연속된 값도 앞자리에 나오면 1개로 바로 정리 가능

# 5. 이모지가 있을 경우 _ 로 치환 --> 4분만 더 할애해보자. 
name = re.sub(emoji_pattern,"_",name) # re.compile한 값을 -> _ 패턴으로 -> name 문자열에서 변경한다.

if name[0] in "._/": # 3. 첫번째 특수문자 안되는 것 제거
	name = name.replace(name[0],'')
		
# 7. 빈 텍스트일 경우, 임의로 된 숫자 5자리 넣기
if name == '':
	for i in range(5):
		name += str(random.randint(0,9))
print(name)