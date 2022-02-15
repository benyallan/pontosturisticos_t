from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):

    user = models.ForeignKey(User, verbose_name=("usuário"), 
                             on_delete=models.CASCADE)
    comentario = models.TextField(("comentário"), 
                                  null=True, blank=True)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("avaliação")
        verbose_name_plural = ("avaliações")

    def __str__(self):
        return self.user.username
