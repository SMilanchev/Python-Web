from django import forms
from django.core.validators import MinLengthValidator


def validate_name(value):
    if value[0].islower():
        raise forms.ValidationError('The name must start with an uppercase letter.')


def validate_age(value):
    if value < 0:
        raise forms.ValidationError('The age cannot be less than zero.')


def validate_email(value):
    if '.' and '@' not in value:
        raise forms.ValidationError('Enter a valid email.')


def validate_password(value):
    if not value.isalnum():
        raise forms.ValidationError('Enter a valid password.')


class UserForm(forms.Form):
    name = forms.CharField(
        validators=[
            MinLengthValidator(6),
            validate_name,
        ],
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(),
        validators=[
            validate_age,
        ],
    )
    email = forms.EmailField(
        widget=forms.EmailInput(),
        validators=[
            validate_email,
        ],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[
            MinLengthValidator(8),
            validate_password,
        ],
    )
    text = forms.CharField(
        widget=forms.Textarea(),
    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        max_length=0,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']

        if value:
            raise forms.ValidationError('This form was created by a bot')

    # def clean_password(self):
    #     pure_password = self.cleaned_data['password']
    #     return f'!{pure_password}!'