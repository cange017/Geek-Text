from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django import forms

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class ShippingAddress(models.Model):
    address = models.CharField("Address", max_length=128)
    city = models.CharField("City", max_length=64)
    state = models.CharField("State", max_length=128, default='FL')
    zipcode = models.CharField("Zipcode", max_length=5)

    class Meta:
        verbose_name_plural = 'ShippingAddress'

    def __str__(self):
        return self.name


class Payment(models.Model):
    name_on_card = forms.CharField(max_length=50)
    cc_number = CardNumberField(('card number'))
    cc_expiry = CardExpiryField(('expiration date'))
    cc_code = SecurityCodeField(('security code'))

    class Meta:
        verbose_name_plural = 'Payment'

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name = "email", max_length=254, unique = True)
    username = models.CharField( max_length=30, unique = True)
    
    first_name = models.CharField(max_length =30,blank=True, null=True)
    last_name = models.CharField(max_length = 30,blank=True, null=True)

    shipping_address = models.ManyToManyField('ShippingAddress',related_name='user')
    credit_card = models.ManyToManyField('Payment',related_name='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

class Address(models.Model):
    address = models.CharField("Address", max_length=128)
    city = models.CharField("City", max_length=64)
    state = models.CharField("State", max_length=128, default='FL')
    zipcode = models.CharField("Zipcode", max_length=5)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'address', null= True)

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.address


   
        
    
    