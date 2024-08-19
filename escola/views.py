from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics

class EstudanteViweSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']) #pk de primary key o kwargs é um dicionario que pega todas as informações listadas e salva
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Curso.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer  





"""
COMEÇOU ASSIM, MAS DEPOIS MUDOU TUDO!!!!

from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'tiago'
        }
        return JsonResponse(estudante)
"""