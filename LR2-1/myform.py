from bottle import post, request
import re

@post('/home', method='post')
def my_form():
    return check()

def check():
    regex = r'\w+\@\w+\.\w[2-3]'
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    answer = " "
    if (len(mail) == 0  | len(question) == 0):
        answer = "Please, fill down the form fields."
    elif (mail != re.search(regex, mail)):
        answer = "You've entered an incorrect email. Please try again with your email or create a new one"
    else:
        answer = "Thanks! The answer will be sent to the mail %s" % mail
    return answer