from bottle import post, request
import re
import pdb
import json

@post('/home', method='post')
def my_form():
    return check()

def check():
    regex = r'\w+\@\w+\.\w[2-3]'
    answer = " "
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    questions = {}
    questions['people'] = []
    questions['people'].append({
        'mail' : mail,
        'question' : question})
    with open('data.txt', 'w') as outfile:
        json.dump(questions, outfile)
    answer = "Thanks! The answer will be sent to the mail %s" % mail
    return answer
#if (len(mail) == 0  | len(question) == 0):
        #answer = "Please, fill down the form fields."
    #elif (mail != re.search(regex, mail)):
        #answer = "You've entered an incorrect email. Please try again with your email or create a new one"
    #else:
        #answer = "Thanks! The answer will be sent to the mail %s" % mail