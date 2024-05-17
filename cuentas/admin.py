from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioPrincipalFormularioCreacion, UsuarioPrincipalFormularioCambio
from .models import UsuarioPrincipal


class UsuarioPrincipalAdmin(UserAdmin):
    add_form = UsuarioPrincipalFormularioCreacion
    form = UsuarioPrincipalFormularioCambio
    model = UsuarioPrincipal
    list_display = [
        "email",
        "username",
        "nombre",
        "is_staff",
    ]


fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("nombre",)}),)
add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("nombre",)}),)

admin.site.register(UsuarioPrincipal, UsuarioPrincipalAdmin)
