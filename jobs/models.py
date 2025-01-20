import random

from django.db import models

# Create your models here.
from django.utils.timezone import now
from django.utils.text import slugify

from users.models import User





class GeneralClass(models.Model):
    title = models.CharField(max_length=150, default="")
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(default="")
    create_date = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.title:  # Generar slug si no existe
            self.slug = slugify(self.title) + str(random.randint(10, 99))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True



class Incidencias(GeneralClass):
    """Model definition for Incidencias."""

    TYPE_CHOICES =[
        ("bug", "bug"),
        ("feature", "feature"),
        ("task", "task")
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    priority = models.PositiveSmallIntegerField(default=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incidencias")
    
    due_date = models.DateTimeField(null=True, blank=True)
    


    class Meta:
        """Meta definition for Incidencias."""

        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

    def __str__(self):
        """Unicode representation of Incidencias."""
        return f"{self.type}: {self.title}-{self.progress}"


class HistoriaUsuario(GeneralClass):
    """Model definition for HistoriaUsuario."""

    incidencia = models.ForeignKey(Incidencias, on_delete=models.CASCADE, related_name="historias")
    estimate_time = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)    


    class Meta:
        """Meta definition for HistoriaUsuario."""

        verbose_name = 'Historia de Usuario'
        verbose_name_plural = 'Historias de Usuarios'

    def __str__(self):
        """Unicode representation of HistoriaUsuario."""
        return self.title
    


class Tareas(GeneralClass):
    """Model definition for Tareas."""

    STATE_CHOICES = [
        ("pending", "pending"),
        ("in progress", "in progress"),
        ("completed", "completed")
    ]    

    state = models.CharField(max_length=15, choices=STATE_CHOICES)
    active = models.BooleanField(default=False)
    user_history = models.ForeignKey(HistoriaUsuario, on_delete=models.CASCADE, related_name="tareas")

    class Meta:
        """Meta definition for Tareas."""

        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        """Unicode representation of Tareas."""
        return self.title
    


class Comentarios(models.Model):
    """Model definition for Comentarios."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios")
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    incidencia = models.ForeignKey(Incidencias, on_delete=models.CASCADE, related_name="comentarios", null=True, blank=True)
    user_history = models.ForeignKey(HistoriaUsuario, on_delete=models.CASCADE, related_name="comentarios", null=True, blank=True)
    jobs = models.ForeignKey(Tareas, on_delete=models.CASCADE, related_name="comentarios", null=True, blank=True)

    class Meta:
        """Meta definition for Comentarios."""

        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        """Unicode representation of Comentarios."""

        if self.incidencia:
            place = "incidencia"
        elif self.jobs:
            place = "Tarea"
        elif self.user_history:
            place = "Historia de usuario"
        else:
            place = "sin asignar"

        return f"{self.user}: comentó en {place}"
