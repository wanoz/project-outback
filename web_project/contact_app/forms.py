from django import forms
from django.core import validators

# Custom form input validator
def check_feedback(value):
    # Profanity filter
    profanity_words = [
        "idiot",
        "suck",
        "dumb",
        "fuck",
        "die",
        "dick",
        "go to hell",
    ]
    
    for word in profanity_words:
        if (word in value.lower()) == True:
            raise forms.ValidationError("Please avoid using inappropriate language.")
            break

    
# Create forms
class Contact_forms(forms.Form):
    feedback = forms.CharField(
        label = '',
        widget=forms.Textarea(attrs={
            'class' : 'form-control',
            'placeholder' : 'Any questions or concerns. Let us know how we can better serve you.',
            'rows' : '5',
        }),
        validators=[check_feedback],
    )

    recommendation = forms.ChoiceField(
        label = 'Would you recommend this to your friends or family?',
        choices=(
            ('0', 'Select...'), 
            ('1', 'Yes'),
            ('2', 'No'), 
            ('3', 'Maybe')
        ),
        widget=forms.Select(attrs={
            'class' : 'custom-select mb-2 mr-sm-2 mb-sm-0',
            'id' : 'inlineFormCustomSelectPref',
        }),
    )

    email = forms.EmailField(
        label = "Email (optional, we'll notify you on future updates)",
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'e.g. name@...mail.com',
        })
    )

    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

