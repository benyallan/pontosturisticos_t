from core.models import PontoTuristico
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from rest_framework import serializers


class PontoTuristicoSerializer(ModelSerializer):
    
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentario = ComentarioSerializer(many=True)
    avaliacao = AvaliacaoSerializer(many=True)
    
    descricao_completa = serializers.SerializerMethodField()
    
    class Meta:
        model = PontoTuristico
        fields = [
                    'id', 'nome', 'descricao', 'aprovado', 'atracoes', 
                    'comentario', 'avaliacao', 'endereco', 'foto',
                    'descricao_completa', 'descricao_completa2'
                ]
    
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
    