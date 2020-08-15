from django import forms
from shortner.models import Shortner


class ShortnerForm(forms.Form):
	short_url = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'https://example.com', 'class': 'form-control'}), error_messages={'required': 'You must enter an alias'})
	original_url = forms.URLField(widget= forms.TextInput(attrs={'placeholder': 'Enter an alias..', 'class': 'form-control', 'maxlength': 100}), error_messages={'required': 'YYou must enter a URL'})
	class Meta:
		fields = ('short_url', 'original_url')
