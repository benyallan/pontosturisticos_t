from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    lookup_field = 'nome'
    queryset = PontoTuristico.objects.all()
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
            
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
            
        
        if descricao:
            queryset = queryset.filter(descricao=descricao)
            
        
        return queryset
        
    
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
        
    
    @action(detail=True, methods=['get'])
    def denunciar(self, request, pk=None):
        return Response({'Mensagem': 'denunciado!'})
    