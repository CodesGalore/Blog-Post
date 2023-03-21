from django import forms
from .models import MomentsToDocument

class AddingMomentForm(forms.ModelForm):
	class Meta:
		model = MomentsToDocument
		fields = ('title_Of_Moment','created_by','date_Of_Moment','body_Text_Of_Moment')



		labels = {
        "title_Of_Moment":  "Moment Title ",
        "body_Text_Of_Moment": "Moment Text ",
   		}


		widgets = {

			'title_Of_Moment': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your title here. Can be anything!'}),
			'created_by': forms.TextInput(attrs={'class':'form-control','value':'','id':'creator','type':'hidden'}),

			'date_Of_Moment': forms.TextInput(attrs={'class':'form-control','placeholder': 'Month Day, Year'}),
			'body_Text_Of_Moment': forms.Textarea(attrs={'class':'form-control','placeholder': 'Write about your moment here!'}),
		}


class UpdatingMomentForm(forms.ModelForm):
	class Meta:
		model = MomentsToDocument
		fields = ('title_Of_Moment','date_Of_Moment','body_Text_Of_Moment')


		labels = {
        "title_Of_Moment":  "Moment Title",
        "body_Text_Of_Moment": "Moment Text",
   		}


		widgets = {

			'title_Of_Moment': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your title here. Can be anything!'}),
			'date_Of_Moment': forms.TextInput(attrs={'class':'form-control','placeholder': 'Month Day, Year'}),
			'body_Text_Of_Moment': forms.Textarea(attrs={'class':'form-control','placeholder': 'Write about your moment here!'}),
		}