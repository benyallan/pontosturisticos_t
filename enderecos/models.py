from django.db import models

class Endereco(models.Model):

    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(("país"), max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = ("endereço")
        verbose_name_plural = ("endereços")

    def __str__(self):
        return self.linha1
