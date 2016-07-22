from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=80, required=False)
    last_name = forms.CharField(max_length=80, required=False)
    message = forms.CharField(widget=forms.Textarea)
