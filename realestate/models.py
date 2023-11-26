from account.models import User
from django.db import models


# Create your models here.


# مدل استان برای اینکه کاربر بتواند استان خود را انتخواب کند
class State(models.Model):
    name = models.CharField(verbose_name='نام استان', max_length=1000)

    def __str__(self):
        return self.name


# مدل شهر برای اینکه کاربر بتواند شهر خود را انتخواب کند

class City(models.Model):
    name = models.CharField(verbose_name='نام شهر', max_length=1000)

    def __str__(self):
        return self.name


# مدل مدل ملک برای اینکه کاربر بتواند نوع ملک خود را انتخواب کند

class PropertyModel(models.Model):
    name = models.CharField(verbose_name='نام مدل ملک ها', max_length=1000)

    def __str__(self):
        return self.name


# مدل نوع ملک برای اینکه کاربر بتواند نوع ملک خود را انتخواب کند

class PropertyType(models.Model):
    name = models.CharField(verbose_name='نام مدل ملک ها ', max_length=1000)

    def __str__(self):
        return self.name


# مدل امکانات ملک ملک برای اینکه کاربر بتواند امکانات ملک خود را انتخواب کند

class PropertyPossibilities(models.Model):
    name = models.CharField(verbose_name='نام امکانات', max_length=1000)

    def __str__(self):
        return self.name


# مدل نوع کف ملک برای اینکه کاربر بتواند نوع کف ملک ملک خود را انتخواب کند

class TypeFloorProperty(models.Model):
    name = models.CharField(verbose_name='نام نوع کف ها برای ملک ها ', max_length=1000)

    def __str__(self):
        return self.name


# مدل سیستم گرماییشی ملک  برای اینکه کاربر بتواند سیستم گرماییشی ملک خود را انتخواب کند

class HeatingSystemProperty(models.Model):
    name = models.CharField(verbose_name='نام سیستمای گرمایشی ', max_length=1000)

    def __str__(self):
        return self.name


# مدل سیستم سرمایشی ملک  برای اینکه کاربر بتواند سیستم سرمایشی ملک خود را انتخواب کند

class CoolingSystemProperty(models.Model):
    name = models.CharField(verbose_name='نام سیستمای سرمایشی ', max_length=1000)

    def __str__(self):
        return self.name


class SelectionSans(models.Model):
    name = models.CharField(verbose_name='نام سانس ها ', max_length=1000)

    def __str__(self):
        return self.name


class KitchenEquipment(models.Model):
    name = models.CharField(verbose_name='نام تجهیزات اشپز خانه ', max_length=1000)

    def __str__(self):
        return self.name


class WelfarePossibilities(models.Model):
    name = models.CharField(verbose_name='نام اکانات رفاهی ', max_length=1000)

    def __str__(self):
        return self.name


class EntertainmentPossibilities(models.Model):
    name = models.CharField(verbose_name='نام سرگرمی ها ', max_length=1000)

    def __str__(self):
        return self.name


class OtherSpacesResidence(models.Model):
    name = models.CharField(verbose_name='نام دیگر فضاهای اقامتگاه ', max_length=1000)

    def __str__(self):
        return self.name


class EnvironmentalContext(models.Model):
    name = models.CharField(verbose_name='نام بافت های محیطی', max_length=1000)

    def __str__(self):
        return self.name


class BedCount(models.Model):
    name = models.CharField(verbose_name='نام تعداد تخت ها', max_length=1000)

    def __str__(self):
        return self.name


class RoomPossibilities(models.Model):
    name = models.CharField(verbose_name='نام امکانات اتاق', max_length=1000)

    def __str__(self):
        return self.name


class TypeOwnership(models.Model):
    name = models.CharField(verbose_name='مالیکت ها', max_length=1000)

    def __str__(self):
        return self.name


# مدل ثبت اطلاعات ماک دار
class PropertyInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property')
    owner_name = models.CharField(verbose_name='نام ملک', max_length=1000)
    state = models.ForeignKey(State, verbose_name='استان', on_delete=models.CASCADE, related_name='property')
    city = models.ForeignKey(City, verbose_name='شهر', on_delete=models.CASCADE, related_name='property')
    property_address = models.CharField(verbose_name='ادرس ملک', max_length=1000)
    post_card = models.BigIntegerField(verbose_name='کد پستی')
    property_phone = models.BigIntegerField(verbose_name='تلفن ملک')
    name_property_owner = models.CharField(verbose_name='نام صاحب ملک', max_length=1000)
    phone_property_manager = models.BigIntegerField(verbose_name='شماره تلفن مدیر ملک')
    phone_property = models.BigIntegerField(verbose_name='شماره تلفن ملک')
    square_footage_property = models.IntegerField(verbose_name='متراژ ملک')
    about_property = models.TextField(verbose_name='درباره ملک(اختیاری)', blank=True, null=True)
    created_at_property = models.DateField(verbose_name='ُسال ساخت ملک')
    villa_registration_rules = models.TextField(verbose_name='قوانین ثبت ویلا')
    capacity_property = models.CharField(max_length=100000, verbose_name='ظرفیت ملک')
    lease_date = models.DateField(verbose_name='ﺗﺎرﻳﺦاﺟﺎره(ﺗﺎرﻳﺦ ﻫﺎي آزاد)')
    property_image = models.ImageField(upload_to='images/ads/property', verbose_name='تصاویر ملک')
    property_image2 = models.ImageField(upload_to='images/ads/property', verbose_name='تصاویر ملک')
    property_image3 = models.ImageField(upload_to='images/ads/property', verbose_name='تصاویر ملک')
    property_image4 = models.ImageField(upload_to='images/ads/property', verbose_name='تصاویر ملک')
    enter_limit = models.TimeField(verbose_name='محدودیت ورود')
    exit_limit = models.TimeField(verbose_name='محدودیت خروج')
    property_model = models.ForeignKey(PropertyModel, on_delete=models.CASCADE, verbose_name='مدل ملک')
    type_floor_property = models.ForeignKey(TypeFloorProperty, on_delete=models.CASCADE, verbose_name='نوع کف ملک')
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name='نوع ملک')
    property_possibilities = models.ManyToManyField(PropertyPossibilities, verbose_name='اﻣﻜﺎﻧﺎت ﻣﻠﻚ')
    heating_system_property = models.ForeignKey(HeatingSystemProperty, on_delete=models.CASCADE,
                                                verbose_name='ﺳﻴﺴﺘﻢ گﺮﻣﺎﻳﺶ ملک')
    cooling_system = models.ForeignKey(CoolingSystemProperty, on_delete=models.CASCADE, verbose_name='سیستم سرمایش ملک')
    parking_count = models.SmallIntegerField(verbose_name='تعداد پارکینگ')
    classes = models.SmallIntegerField(verbose_name='طبقه')
    image = models.ImageField(upload_to='images/ads/property/bills', verbose_name='قبض تلفن یا برق یا گاز')
    selection_sans = models.ForeignKey(SelectionSans, on_delete=models.CASCADE, verbose_name='انتخاب سانس')
    lease_price = models.IntegerField(verbose_name='قیمت اجاره')
    property_number = models.BigIntegerField(verbose_name='شماره ملک')
    days_booking = models.CharField(max_length=1000000000, verbose_name='روز های ازار برای رزرو')
    # Bank information.
    shaba_number = models.BigIntegerField(verbose_name='شماره شبا')
    cart_number = models.BigIntegerField(verbose_name='شماره کارت')
    account_number = models.BigIntegerField(verbose_name='شماره حساب')
    # End
    melli_cart = models.ImageField(upload_to='images/ads/property/documents', verbose_name='کارت ملی یا شناسنامه')
    discount = models.BooleanField(default=False)
    residence_rules = models.TextField(max_length=100000000, verbose_name='قوانین اقامت')
    cancel_request = models.TextField(max_length=100000000, verbose_name='قوانین لغو درخواست(کنسلی)')
    kitchen_equipment = models.ManyToManyField(KitchenEquipment, verbose_name='تجهیزات اشپزخانه')
    entertainment_possibilities = models.ManyToManyField(EntertainmentPossibilities, verbose_name='ُسرگرمی ها')
    # booking rules.
    enter_time = models.TimeField(verbose_name='ساعت ورود')
    exit_time = models.TimeField(verbose_name='ساعت خروج')
    minimum_stay_limit = models.CharField(max_length=100000, verbose_name='حداقل شب اقامت')
    maximum_stay_limit = models.CharField(max_length=10000, verbose_name='حداکثر مدت اقامت')
    welfare_possibilities = models.ManyToManyField(WelfarePossibilities, verbose_name='امکانات رفاهی')
    other_spaces_residence = models.ManyToManyField(OtherSpacesResidence, verbose_name='سایر فضاهای اقامتگاه')
    environmental_context = models.ForeignKey(EnvironmentalContext,on_delete=models.CASCADE ,verbose_name='بافت محیطی')
    # Bedrooms Information.
    room_title = models.CharField(max_length=10000, verbose_name='عنوان اتاق')
    slug = models.SlugField(max_length=1000)
    bed_count = models.ForeignKey(BedCount, on_delete=models.CASCADE, verbose_name='تعداد تخت ها')
    room_possibilities = models.ManyToManyField(RoomPossibilities, verbose_name='امکانات اتاق')
    type_ownership = models.ForeignKey(TypeOwnership, on_delete=models.CASCADE, verbose_name='نوع مالکیت')
    is_public = models.BooleanField(default=False)
    is_reserve = models.BooleanField(default=False)




class Comment(models.Model):
    property_post = models.ForeignKey(PropertyInformation, on_delete=models.CASCADE, related_name='comment', verbose_name='اگهی ملک')
    name = models.CharField(max_length=1000, verbose_name='نام' )
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='realestatecomment' , verbose_name='کاربر')
    body = models.TextField(max_length=10000000, verbose_name=' نظر')
    rate = models.IntegerField()
    it_good = models.BooleanField(default=False, verbose_name='پیشنهاد میکنید؟')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='reply', verbose_name='ریپلای')

    def __str__(self):
        return self.name
    
