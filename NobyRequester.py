#  -*- coding: UTF-8 -*-
import requests
import urllib 

apikey=""
url ="https://app.cotogoto.ai/webapi/noby.json"
text="今日の名古屋の天気は？"
param = "appkey=" +apikey + "&text=" + text 
print(param)

import sys

r=requests.get(url+'?'+param)
print(r)
file=open("outfile.txt",mode='w')
res = str(r.content,encoding='utf-8')
print(res,file=file)
