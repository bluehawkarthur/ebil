from django import forms, http
# from captcha.fields import CaptchaField
# from captcha.fields import ReCaptchaField
from nocaptcha_recaptcha.fields import NoReCaptchaField
from django.contrib.auth.forms import AuthenticationForm
import socket


REMOTE_SERVER = "www.google.com"
def is_connected():
	try:
	    # see if we can resolve the host name -- tells us if there is
	    # a DNS listening
	    host = socket.gethostbyname(REMOTE_SERVER)
	    # connect to the host -- tells us if the host is actually
	    # reachable
	    s = socket.create_connection((host, 80), 2)
	    print "conectado"
	    return True
	except:
		pass
		return False
		print is_connected()

class LoginForm(AuthenticationForm):
    # captcha = CaptchaField()
    pass
    # if is_connected():
    # 	captcha = NoReCaptchaField()
    # else:
    # 	pass