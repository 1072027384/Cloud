import  requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '1584684399307'


def git_sign():
    return 'b2ba12b30ffe0261057d8e59fcbe39cc'


def get_ts():
    return '18468439930'
    "1585617233708"


form_data={
'i':'你和我都是',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt': get_salt(),
'sign': git_sign(),
'ts': get_ts(),
'bv':'4b9de992aa3d23c2999121d735e53f9c',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME'
}

response=requests.post(url,data=form_data)
print(response.text)
