from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUsers(UserCreationForm):
	email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control','placeholder': 'example123@(email provider).com'}))
	first_name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self,*args,**kwargs):
		super(RegisterUsers,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


	def save(self,commit = True):
		user = super(RegisterUsers,self).save(commit = False)

		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()

		return user