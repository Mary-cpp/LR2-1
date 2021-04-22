from bottle import post, request

@post('/home', method='post')
def my_form():
    return check()

def check():
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    answer = " "
    if (len(mail) == 0  | len(question) == 0):
        answer = "Please, fill down the form fields."
    else:
        answer = "Thanks! The answer will be sent to the mail %s" % mail
    return answer