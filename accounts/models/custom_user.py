from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(
        verbose_name="Nombre",
        max_length=255
    )
    last_name = models.CharField(
        verbose_name="Apellido",
        max_length=255
    )
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True
    )
    username = models.CharField(
        verbose_name="Usuario",
        max_length=255,
        unique=True
    )
    birth_date = models.DateField(
        verbose_name="Fecha de nacimiento",
        max_length=255
    )
    phone_number = models.CharField(
        verbose_name="Número de teléfono",
        max_length=255,
        unique=True
    )
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "birth_date", "phone_number"]
