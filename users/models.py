from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, verbose_name="Nombre de usuario", unique=True)
    names = models.CharField(max_length=50, verbose_name="Nombres")
    lastnames = models.CharField(max_length=50, verbose_name="Apellidos") 
    email = models.EmailField()
    
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.names + ' ' + self.lastnames
    
    def __str__(self):
        return self.username + ': ' + self.get_full_name()
    

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"