from django import forms
from django.core.exceptions import ValidationError

from todos_app.todos.models import Todo
from todos_app.todos.validators import validate_owner_todos_count


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        # fields = ['title', 'description', 'state', 'owner']
        exclude = ('categories', )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'owner': forms.RadioSelect(),

        }

    def clean(self):
        validate_owner_todos_count(self.cleaned_data['owner'])


    #
    # def clean_title(self):
    #     validate_dot(self.cleaned_data['title'])


class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        validators=[
            # validate_dot,
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter todo text',
            }
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
                'placeholder': 'Enter todo description'
            }
        )
    )

    # bots_catcher = forms.CharField(
    #     widget=forms.HiddenInput(),
    #     required=False,
    # )
    #
    # def clean_bots_catcher(self):
    #     value = self.cleaned_data['bots_catcher']
    #
    #     if value:
    #         raise forms.ValidationError('U are a bot')

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bots_catcher(self):
        value = self.cleaned_data['bots_catcher']

        if value:
            raise forms.ValidationError('u are a bot')

#
# class UpdateTodoForm(CreateTodoForm):
#     state = forms.BooleanField()
