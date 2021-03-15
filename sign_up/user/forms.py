from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user
