from django.db import models
from realestate.models import State
from account.models import User
# Create your models here.

class CookType(models.Model):
    name = models.CharField(max_length=1000, verbose_name='نوع غذا')

    def __str__(self) -> str:
        return self.name
    
class ChefInformation(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='chefs' , verbose_name='کاربر')
    number = models.IntegerField(verbose_name='شماره ثابت')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='food', verbose_name='نام استان')
    address = models.TextField(max_length=10000, verbose_name='ادرس')
    how_much_cook = models.IntegerField(verbose_name='توانایی چند پخت درروز را دارید')
    what_can_cook = models.ForeignKey(CookType, on_delete=models.CASCADE, related_name='food', verbose_name=' نوع غذایی میتوانید درست کنید')
    number = models.IntegerField(verbose_name='تعداد')
    date_cook = models.CharField(max_length=1000, verbose_name=' روز هایی میتوانید غذا درست کنید')
    time_cook = models.TimeField(verbose_name='ساعت هایی که می توانید غذا درست کنید')
    master_chef_name = models.CharField(max_length=1000, verbose_name='نام سر اشپز')
    chef_name = models.CharField(max_length=1000, verbose_name='نام اشپز')
    image_1   = models.ImageField(upload_to='images/ads/food/image', verbose_name='اپلود عکس از غذا')
    image_2 = models.ImageField(upload_to='images/ads/food/image', verbose_name='اپلود عکس از غذا')
    image_3 = models.ImageField(upload_to='images/ads/food/image', verbose_name='اپلود عکس از غذا')
    point = models.IntegerField(verbose_name='امتیاز')
    is_public = models.BooleanField(default=False)


class Comment(models.Model):
    food_post = models.ForeignKey(ChefInformation , on_delete=models.CASCADE, related_name='comment', verbose_name='اگهی اتوبوس')
    name = models.CharField(max_length=1000, verbose_name='نام' )
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='comment' , verbose_name='کاربر')
    it_good = models.BooleanField(default=False, verbose_name='پیشنهاد میکنید؟')
    rate = models.IntegerField()
    body = models.TextField(max_length=10000000, verbose_name='جزعیات نظر')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='reply', verbose_name='ریپلای')

    def __str__(self):
        return self.name