from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import permissions

from cursos.models import Curso, Avaliacao
from cursos.api.serializers import AvaliacaoSerializer, CursoSerializer
from cursos.permissions import EhSuperUser

class CursoViewSet(viewsets.ModelViewSet):
    """ 
    API de Cursos da geek 
    """
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,)

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        """
        Retorna as avaliações de um curso
        """
      
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


""" class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer """


class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
