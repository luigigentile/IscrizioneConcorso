from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

from users.forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # queste due istruzioni permettono di aggiungere ulteriori campi a User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email' ,'is_staff','ruolo','telefono','fax']


admin.site.register(CustomUser,CustomUserAdmin)
