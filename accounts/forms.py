from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _



class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})




attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs=attrs)
    )


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=attrs)
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(attrs=attrs)
    )
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2 = forms.CharField(
        label=_('Password Confirmation'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')
    


    def delete_user(self):
        if self.instance.username == self.cleaned_data['username']:
            self.instance.delete()
            return True
        return False


class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

