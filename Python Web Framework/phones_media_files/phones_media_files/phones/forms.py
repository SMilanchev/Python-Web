from django import forms

from phones_media_files.phones.models import Phone, PhoneImage


class PhoneForm(forms.ModelForm):
    image = forms.ImageField()

    def save(self, commit=True):
        phone = super().save(commit=commit)

        phone_image = PhoneImage(
            image=self.cleaned_data['image'],
            is_selected=True,
            phone=phone
        )

        if commit:
            phone_image.save()

        return phone

    class Meta:
        model = Phone
        fields = '__all__'
