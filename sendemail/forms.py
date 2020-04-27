from django import forms
from . models import Abc

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class AbcForm(forms.ModelForm):
	class Meta:
		model = Abc
		fields = ['aaa', 'bbb', 'flagcalc']