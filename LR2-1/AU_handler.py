from bottle import post, request, template
import json
from datetime import datetime

@post('/activeUsers', method='post')
def reading():
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['question']:
            emails = []
            emails.append(p['mail'])
            print('Mail:' + p['mail'])
    return template('activeUsers.tpl', title='Active Users', message='The most Active Users on our website', year=datetime.now())
