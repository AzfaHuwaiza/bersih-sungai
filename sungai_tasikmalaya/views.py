from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .views import *
from .serializers import *
from .models  import *



# View Register / Daftar
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
 
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Akun berhasil dibuat! Silakan login untuk melanjutkan.')
            return redirect('login')
    else:
        form = CustomRegisterForm()
        
    return render(request, 'sungai_tasikmalaya/register.html', {'form': form})

# View Login / Masuk
def login_view(request):
    if request.user.is_authenticated:
            return redirect('home')

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Tambahkan argumen backend saat memanggil authenticate
            user = authenticate(request, username=username, password=password, backend='path.to.EmailOrUsernameModelBackend')  # Ganti dengan path yang sesuai
            if user is not None:
                login(request, user)
                return redirect('home')  # Ganti 'home' dengan URL yang sesuai
    else:
        form = CustomLoginForm()

    return render(request, 'sungai_tasikmalaya/login.html', {'form': form})

# View Logout / Keluar
def logout_view(request):
    logout(request)  # Logout pengguna
    return redirect('login')  

# View Home / Beranda
@login_required
def home_view(request):
    return render(request, 'sungai_tasikmalaya/home.html')

# My Profile
@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'sungai_tasikmalaya//profil/profil.html', {'profile': profile})

# View Edit Profile
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form  = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profil berhasil diperbarui!')
            return redirect('my_profile')

    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'sungai_tasikmalaya/profil/edit_profile.html', context)

