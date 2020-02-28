from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser




class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Add a valid email address.')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ( 'first_name','last_name','email', 'username', 'password1', 'password2', )

class LoginForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = CustomUser
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")



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