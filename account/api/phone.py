from django.conf import settings 
from account.models import User 
from django.core import mail 
from random import randint
import ghasedakpack
import requests

sms = ghasedakpack.Ghasedak("")
 
def send_otp_via_phone(phone): 
    subject = 'Your account verification phone' 
    random_code = randint(1000, 9999) 
    sms.verification({'receptor': phone , 'type': '1','template': 'musicapp','param1': random_code})
    user_obj = User.objects.get(phone=phone) 
    user_obj.otp = random_code 
    user_obj.save()