from rest_framework import viewsets
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'descricao')