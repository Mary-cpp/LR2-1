from bottle import post, request
import re
import pdb
import json

questions = {}
questions['question'] = []

@post('/home', method='post')
def my_form():
    return check()

def check():
    regex = re.compile(r'\w+@\w+\.\w')
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    if (len(mail) == 0  | len(question) == 0):
        return "Please, fill down the form fields."
    elif regex.match(mail):
        questions['question'].append({'mail' : mail, 'question' : question})
        with open('data.txt', 'w') as outfile:
            json.dump(questions, outfile)
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "You've entered an incorrect email. Please try again with your email or create a new one"
