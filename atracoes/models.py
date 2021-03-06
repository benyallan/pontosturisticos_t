from django.db import models

class Atracao(models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.TextField("descrição")
    horario_func = models.CharField(("horário de funcionamento"), 
                                    max_length=25)
    idade_minima = models.IntegerField(("idade mínima"))
    foto = models.ImageField(
                                upload_to='atracoes', 
                                null=True, blank=True
                             )

    class Meta:
        verbose_name = ("atração")
        verbose_name_plural = ("atrações")

    def __str__(self):
        return self.nome
