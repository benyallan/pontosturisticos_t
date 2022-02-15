# Generated by Django 4.0.2 on 2022-02-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('avaliacoes', '0001_initial'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao', verbose_name='avaliação'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentario',
            field=models.ManyToManyField(to='comentarios.Comentario', verbose_name='comentário'),
        ),
    ]