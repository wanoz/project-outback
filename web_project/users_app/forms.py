from django import forms
from django.core import validators
from django.contrib.auth.models import User
from users_app.models import User_profile_db

class User_basic_form(forms.ModelForm):
    username = forms.CharField(
        label = 'Username:',
        widget=forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )
    
    password = forms.CharField(
        label = 'Password:',
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control'
        })
    )

    email = forms.EmailField(
        label = 'Email:',
        widget=forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class User_profile_form(forms.ModelForm):
    vegetarian = forms.ChoiceField(
        label = 'Are you vegetarian?',
        choices=(
            ('0', 'Select...'), 
            ('1', 'Yes'),
            ('2', 'No'), 
        )
    )

    food_allergy = forms.CharField(
        label = 'Specify any food allergy, or state "no" otherwise:',
        widget=forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )

    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    class Meta:
        model = User_profile_db
        fields = ('vegetarian', 'food_allergy')