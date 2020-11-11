from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder' : "Name"
            }
            ))
    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder' : "Email"
            }
        ))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'placeholder' : "Message"
            }
        ))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = ""
        self.fields['contact_email'].label = ""
        self.fields['content'].label = ""