import  requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
from_data={
'i':'你和我都是',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'1584684399307',
'sign':'b2ba12b30ffe0261057d8e59fcbe39cc',
'ts':'18468439930',
'bv':'4b9de992aa3d23c2999121d735e53f9c',
'doctype':'json',
'version':'2.1',
'keyfrom:'fanyi.web',
'action':'FY_BY_REALTlME'}

response=requests.post(url,form_date)
print(response.text)


