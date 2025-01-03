from django import forms
from django.contrib.auth import authenticate

from .models import User



class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña"
            }
        )
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir Contraseña"
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "names",
            "lastnames",
            "email"
        )

    def clean_password1(self):
        if len(self.cleaned_data.get("password1")) <= 5:
            self.add_error("password1", "La contraseña debe tener 6 o más caracteres")

    def clean_password2(self):
        if self.cleaned_data.get("password1") != self.cleaned_data.get("password2"):
            self.add_error("password2", "Las contraseñas deben coincidir")



class LoginForm(forms.Form):

    username = forms.CharField(
        label="Nombre de usuario",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de usuario",
                "style": "{ margin: 10px }"
            }
        )
    )

    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña"
            }
        )
    )


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos del usuario no son correctos")

        return cleaned_data
