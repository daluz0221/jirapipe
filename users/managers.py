from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, names, lastnames, password, is_staff, is_superuser, **kwargs):
        if is_superuser:
            user = self.model(
                username=username,
                names="Luis Felipe",
                lastnames="Echeverry Parra",
                email=email,
                is_staff=is_staff,
                is_superuser=is_superuser,
                **kwargs
            )
        else:
            user = self.model(
                username=username,
                names=names,
                lastnames=lastnames,
                email=email,
                is_staff=is_staff,
                is_superuser=is_superuser,
                **kwargs
            )
        
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, names, lastnames, password=None, **kwargs):
        return self._create_user(username, email, names, lastnames, password, False, False, **kwargs)
        

    def create_superuser(self, username, email, password=None, **kwargs):
        return self._create_user(username, email, "", "", password, True, True, **kwargs)

