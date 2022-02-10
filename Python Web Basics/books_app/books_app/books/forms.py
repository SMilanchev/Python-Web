from django import forms

from books_app.books.models import Book, Author


# class BookForm(forms.ModelForm):
#     author_name = forms.CharField(
#         max_length=20,
#     )
#
#     def save(self, commit=True):
#         author = Author(
#             name=self.cleaned_data['author_name']
#         )
#         author.save()
#         self.instance.author = author
#         return super().save(commit)
#
#     class Meta:
#         model = Book
#         fields = ('title', 'description', 'pages', 'author_name')
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'pages': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'author': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'description': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             )
#         }


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class BookForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Book
        fields = ('title', 'description', 'pages')
        widgets = {
            'title': forms.TextInput(),
            'pages': forms.NumberInput(),
            'author': forms.TextInput(),
            'description': forms.Textarea()
        }


class AuthorForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Author
        fields = '__all__'


class StateFilterForm(forms.Form):
    state = forms.ChoiceField(
        required=False,
        choices=(
                ('done', "DONE"),
                ('not-done', "NOT-DONE"),
                ('all', "ALL"),
        )
    )
