from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPrincipal


class UsuarioPrincipalFormularioCreacion(UserCreationForm):
    class Meta(UserCreationForm):
        model = UsuarioPrincipal
        fields = UserCreationForm.Meta.fields + ("nombre",)


class UsuarioPrincipalFormularioCambio(UserChangeForm):
    class Meta:
        model = UsuarioPrincipal
        fields = UserChangeForm.Meta.fields
