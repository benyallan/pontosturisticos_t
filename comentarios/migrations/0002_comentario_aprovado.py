# Generated by Django 4.0.2 on 2022-02-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
