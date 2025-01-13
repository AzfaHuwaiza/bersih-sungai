from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *
import re



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email', max_length=254)

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Username dapat berisi karakter apa pun.',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nama Pengguna',
            'first_name': 'Nama Depan',
            'last_name': 'Nama Belakang',
            'email': 'Email',
            'password1': 'Kata Sandi',
            'password2': 'Konfirmasi Kata Sandi',
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email ini sudah digunakan. Silakan gunakan email lain.')
        return email

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        # help_text='Username dapat berisi karakter apa pun.',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance  # Mengacu pada user yang sedang diedit
        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            raise forms.ValidationError('Email ini sudah digunakan. Silakan gunakan email lain.')
        return email


class ProfileForm(forms.ModelForm):
    alamat = forms.CharField(required=False)
    tanggal_lahir = forms.DateField(required=False)
    no_hp = forms.CharField(required=False)
    instagram = forms.CharField(required=False)
    tiktok = forms.CharField(required=False)
    x = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['alamat', 'tanggal_lahir', 'no_hp', 'instagram', 'tiktok', 'x']
