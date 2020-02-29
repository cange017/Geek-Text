from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Address, ShippingAddress, Payment
from django.db import models
from django.forms import formset_factory
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField





class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Add a valid email address.')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ( 'first_name','last_name','email', 'username', 'password1', 'password2', )

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = CustomUser
		fields = ('email', 'username', )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
		except CustomUser.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
		except CustomUser.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class AddressForm(forms.ModelForm):
    address = models.CharField("Address", max_length=128)
    city = models.CharField("City", max_length=64)
    state = models.CharField("State", max_length=128, default='FL')
    zipcode = models.CharField("Zipcode", max_length=5)

    class Meta: 
        model = Address
        fields = ('address', 'city', 'state', 'zipcode')

class ShipAddressForm(forms.ModelForm):
    address = models.CharField("Address", max_length=128)
    city = models.CharField("City", max_length=64)
    state = models.CharField("State", max_length=128, default='FL')
    zipcode = models.CharField("Zipcode", max_length=5)

    class Meta: 
        model = ShippingAddress
        fields = ('address', 'city', 'state', 'zipcode')    

class AddCreditForm(forms.ModelForm):
    name_on_card = forms.CharField(max_length=50)
    cc_number = CardNumberField(('card number'))
    cc_expiry = CardExpiryField(('expiration date'))
    cc_code = SecurityCodeField(('security code'))

    class Meta: 
        model = Payment
        fields = ('name_on_card', 'cc_number', 'cc_expiry', 'cc_code')  