# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re, json

user_input = input()
pattern = re.compile(
    '(https):\/\/([\w\.]+)(\/[\w]+)\?([\w]+)=([\w]+)&([\w]+)=([\w]+)'
)  # 'https://www.myrealtrip.com/cities?key_name=Jeju&utm_source=naver_brand'
result = re.search(pattern, user_input).groups()
dic = {
    "protocol": result[0],
    "domain": result[1],
    "path": result[2],
    "query": [{
        result[3]: result[4]
    }, {
        result[5]: result[6]
    }]
}
print("Hello Goorm ->", dic)