# Generated by Django 4.0.2 on 2022-02-07 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0004_pontoturistico_avaliacao_pontoturistico_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco', verbose_name='endereço'),
            preserve_default=False,
        ),
    ]
