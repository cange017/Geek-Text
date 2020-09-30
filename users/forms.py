from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Address, ShippingAddress, Payment
from django.db import models
from django.forms import formset_factory
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.contrib.auth import get_user_model
from i18naddress import InvalidAddress, normalize_address, get_validation_rules



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

    class Meta: 
        model = Address
        fields = ('country_code', 'street_address',  'city', 'country_area','postal_code'  )  
        
    def clean(self):
        clean_data = super(AddressForm, self).clean()
        validation_rules = get_validation_rules(clean_data)
        try:
            valid_address = normalize_address(clean_data)
        except InvalidAddress as e:
            errors = e.errors
            valid_address = None
            for field, error_code in errors.items():
                if field == 'postal_code':
                    examples = validation_rules.postal_code_examples
                    msg = 'Invalid value, use fomat like %s' % examples
                else:
                    msg = ERROR_MESSAGES[error_code]
                self.add_error(field, msg)
        return valid_address or clean_data    

class ShipAddressForm(forms.ModelForm):
    class Meta: 
        model = ShippingAddress
        fields = ('country_code', 'street_address',  'city', 'country_area','postal_code'  )  
        
    def clean(self):
        clean_data = super(ShipAddressForm, self).clean()
        validation_rules = get_validation_rules(clean_data)
        try:
            valid_address = normalize_address(clean_data)
        except InvalidAddress as e:
            errors = e.errors
            valid_address = None
            for field, error_code in errors.items():
                if field == 'postal_code':
                    examples = validation_rules.postal_code_examples
                    msg = 'Invalid value, use fomat like %s' % examples
                else:
                    msg = ERROR_MESSAGES[error_code]
                self.add_error(field, msg)
        return valid_address or clean_data    

class AddCreditForm(forms.ModelForm):
    name_on_card = models.CharField(max_length=50)
    cc_number = CardNumberField(('card number'))
    cc_expiry = CardExpiryField(('expiration date'))
    cc_code = SecurityCodeField(('security code'))

    class Meta: 
        model = Payment
        fields = ('name_on_card', 'cc_number', 'cc_expiry', 'cc_code')  