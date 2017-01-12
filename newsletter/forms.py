from django import forms 

from .models import SignUp


class ContactForm(forms.Form):
    fullname = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullname', 'email']

    def clean_email(self):
        email =self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email