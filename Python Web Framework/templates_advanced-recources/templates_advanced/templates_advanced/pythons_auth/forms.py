from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class SignInForm(AuthenticationForm):
    user = None
    # email = forms.CharField(
    #     max_length=20
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput()
    # )

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            username=self.cleaned_data['email'],
            password=self.cleaned_data['password'])

        if not self.user:
            raise ValidationError('Email and/or password not correct!')

    def save(self):
        return self.user