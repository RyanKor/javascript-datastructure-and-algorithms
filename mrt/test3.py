# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re
user_input = input()
pattern = re.compile('([a-z\w]+\.*)') # 'https://www.myrealtrip.com/cities?key_name=Jeju&utm_source=naver_brand'
# 결과 값은 user_input 값을 가공해서 출력하는 형태? --> 가능하면 user_input을 변경해도 무방한가?
# 결과값 JSON 포맷
dic = {
	"protocol" : "",
	"domain" : "",
	"path" : "",
	"query" : []
}
result = re.findall(pattern, user_input)
result = list(result)
dic["protocol"] = result[0]
dic["domain"] = ''.join(result[1:3])
dic["path"] = "/" + result[4]
dic["query"].append({result[5]:result[6]})
dic["query"].append({result[7]:result[8]})

print (dic)
# print(result)