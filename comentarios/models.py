from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):

    usuario = models.ForeignKey(User, verbose_name=("usuário"), 
                                on_delete=models.CASCADE)
    comentario = models.TextField(("comentário"))
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("comentário")
        verbose_name_plural = ("comentários")

    def __str__(self):
        return self.usuario.username
