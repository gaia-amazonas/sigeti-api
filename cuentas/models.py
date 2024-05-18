from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioPrincipal(AbstractUser):
    nombre = models.CharField(null=True, blank=True, max_length=100)
