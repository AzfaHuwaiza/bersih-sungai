from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'alamat', 'tanggal_lahir', 'no_hp', 'instagram', 'tiktok', 'x')  # Menampilkan field di daftar admin
    search_fields = ('user__username', 'alamat', 'no_hp')  # Menambahkan kolom pencarian

admin.site.register(Profile, ProfileAdmin)
