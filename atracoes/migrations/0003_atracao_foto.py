# Generated by Django 4.0.2 on 2022-02-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_alter_atracao_horario_func'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]
