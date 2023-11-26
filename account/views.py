from django.shortcuts import render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView , View
from uuid import uuid4
from .mixins import LoginRequirdMixins , LogoutRequirdMixins , AddressRequirdMixins
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
import ghasedakpack
import requests
from .form import RegisterForm , OtpForm , Edite_Profile_Form
from random import randint
from .models import OTP, User

sms = ghasedakpack.Ghasedak("")

class OtpRegisterationView(LoginRequirdMixins , FormView):
    template_name = 'account/'
    form_class = RegisterForm
    success_url = reverse_lazy('#home')
    def form_valid(self, form):
        cd = form.cleaned_data
        random_code = randint(1000 , 9999)
        sms.verification({'receptor': cd['phone'] , 'type': '1','template': 'resinabeat','param1': random_code})
        token = str(uuid4())
        OTP.objects.create(phone = cd['phone'] , code = random_code , username=cd['username']
        , Full_name=cd['Full_name'] , email=cd['email'] , is_simple_user=cd['is_simple_user']
        , is_realestate=cd['is_realestate'] , is_bus_driver=cd["is_bus_driver"] , token = token)
        print(random_code)
        return redirect(reverse('account:check_otp') + f'?token={token}')

class CheckOtpCode(LoginRequirdMixins , FormView):
    template_name = 'account/'
    form_class = OtpForm
    success_url = reverse_lazy('#home')
    def form_valid(self, form):
        token = self.request.GET.get('token')
        cd = form.cleaned_data
        if OTP.objects.filter(code=cd['code'],token=token).exists():
            otp = OTP.objects.get(token=token)
            user , is_created = User.objects.get_or_create(phone = otp.phone , username = otp.username , Full_name=otp.Full_name , email=otp.email
            , is_bus_driver=otp.is_bus_driver , is_realestate=otp.is_realestate , is_simple_user=otp.is_simple_user)
            login(self.request , user)
            otp.delete()
            return redirect('#home')
        else:
            form.add_error(cd['code'] , 'this information is not correct')
        return render(self.request , self.template_name , {'form':form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('#home'))
    else:
        return redirect(reverse('#home'))


class ProfileView(LogoutRequirdMixins , TemplateView) :
    template_name = 'account/'


def profile_edite(request):
    if request.user.is_authenticated == True:
        user = request.user
        form = Edite_Profile_Form(instance=user)
        if request.method == 'POST':
            form = Edite_Profile_Form(request.POST  , request.FILES ,instance=user)
            if form.is_valid():
                form.save()
                return redirect('account:profile')
        else:
            form = Edite_Profile_Form(instance=user)
        return render(request , 'account/' , {'form':form})
    else:
        return redirect('#home')




