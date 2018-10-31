# coding=utf-8
import requests
import json


class Turing:

    def __init__(self):
        pass

    def talk(self, msg):
        api_url = 'http://openapi.tuling123.com/openapi/api/v2'
        data = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": msg
                }
            },
            "userInfo": {
                "apiKey": "9ebaa0aa8837443fa3192f7fdaf2f851",
                "userId": "aa"
            }
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(api_url, headers=headers, data=json.dumps(data))
        print(r.json())
        return r.json().get('results')[0].get('values').get('text')


if __name__ == '__main__':
    # Turing.talk(Turing(), "搞什么")
    a= ''
    print not not a
    # str1 = {u'intent': {u'code': 4000}, u'results': [{u'groupType': 0, u'resultType': u'text', u'values': {
    #     u'text': u'\u8bf7\u6c42\u53c2\u6570\u7f3a\u5931\u6216\u683c\u5f0f\u9519\u8bef!'}}]}
    # print(json.dumps(str1).decode('utf-8'))
    # print str1.get('values')
