from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cursos.models import Curso, Avaliacao
from cursos.api.serializers import AvaliacaoSerializer, CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """ 
    API de Cursos da geek 
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        """
        Retorna as avaliações de um curso
        """
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    """ 
    API de Avaliaçoes da geek 
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
