from django.db import models

class State(models.Model):
    name = models.CharField( max_length=1000 , verbose_name='نام استان')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField( max_length=1000 , verbose_name='نام شهر')

    def __str__(self):
        return self.name

class SimpleUserInformation(models.Model):
    GENDER_CHOICES = (
    ("MALE" , "MALE"),
    ('FEMALE', "FEMALE"),
    )
    full_name = models.CharField(max_length=250 , verbose_name='نام و نام خانوادگی')
    state = models.ForeignKey(State , on_delete=models.CASCADE, related_name='simple_users' , verbose_name='استان')
    city = models.ForeignKey(City , on_delete=models.CASCADE, related_name='simple_users' , verbose_name='شهر')
    gender = models.CharField(max_length=550 , choices=GENDER_CHOICES , verbose_name='جنسیت')
    phone_number = models.BigIntegerField(default=0 , verbose_name='شماره تلفن')
    date_of_birth = models.DateField(null=True , blank=True , verbose_name='تاریخ تولد')
    bank_account = models.BigIntegerField(default=0 , verbose_name='شماره حساب')
    full_name_of_account = models.CharField(max_length=550 , verbose_name='نام و نام خانوادگی صاحب حساب')

    def __str__(self) -> str:
        return self.full_name
