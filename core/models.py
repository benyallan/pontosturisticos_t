from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontoTuristico(models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.TextField("descrição")
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, verbose_name=("atrações"))
    comentario = models.ManyToManyField(Comentario, 
                                        verbose_name=("comentário"))
    avaliacao = models.ManyToManyField(Avaliacao, 
                                        verbose_name=("avaliação"))
    endereco = models.ForeignKey(Endereco, 
                                 verbose_name=("endereço"), 
                                 on_delete=models.CASCADE, 
                                 null=True, blank=True)
    foto = models.ImageField(
                                upload_to='pontos_turisticos', 
                                null=True, blank=True
                             )

    class Meta:
        verbose_name = ("ponto turístico")
        verbose_name_plural = ("pontos turísticos")

    def __str__(self):
        return self.nome
    
    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)
    
