# Generated by Django 4.2 on 2025-01-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_historiausuario_is_delete_incidencias_is_delete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
