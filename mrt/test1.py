# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re, random

user_input = '.......This dog........////////   \U0001f602qwfeqwef\U0001F300qwefqwef!\U0001F6FF@#$!@#%!#@$%^'  #input() # '..k'

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+")

# 로직 구성 방법 --> 1 ~ 7번 순서대로 구현하면 안맞는 로직이 있어 순서를 맞춰 진행할 필요는 없다.
# 5. 이모티콘 사용된 것에 대해 찾아낸 후, _로 치환
remove_emoji = emoji_pattern.sub('_', user_input)
# 1. 한글, 영어, 숫자 및 특수문자 ('.','_','/') 포함 정규식 작성
name = re.sub("[^ㄱ-ㅎ가-힣a-zA-Z0-9._/]", '', remove_emoji)

# 4. 특수문자 연속 사용된 경우 (2개 이상) --> 1개로 축약
dot_pattern = re.sub("\.{2,}", '.', name)
slash_pattern = re.sub("\/{2,}", '/', dot_pattern)
bar_pattern = re.sub("_{2,}", '_', slash_pattern)

# 3. 첫번째 특수문자 안되는 것 제거
if bar_pattern[0] in "._/":
    bar_pattern = bar_pattern.replace(bar_pattern[0], '')

# 7. 빈문자열일 경우 --> 문자열 랜덤 정수 5개 채우기
if bar_pattern == '':
    for i in range(5):
        bar_pattern += str(random.randint(0, 9))
# 2. 이름의 길이는 2글자 이상, 20글자 미만
elif len(bar_pattern) == 1:
    for i in range(4):
        bar_pattern += str(random.randint(0, 9))
elif len(bar_pattern) > 19:
    bar_pattern = bar_pattern[:
                              19]  # 20글자 이상인 부분부터 삭제해야함. (20 글자부터!) 즉, 0 ~ 18 까지!
print(bar_pattern)