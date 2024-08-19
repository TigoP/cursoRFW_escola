from django.contrib import admin
from escola.models import Estudante, Curso, Matricula
"""só pra eu lembrar a senha do admin foi Tigo - tigo@tigo.com - 123456"""

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular') #o que quero que apareça no admin
    list_display_links = ('id', 'nome',)
    list_per_page = 20 #quantos estudantes por pagina quero que apareça
    search_fields = ('nome',)

admin.site.register(Estudante, Estudantes) #modelo e modelo admin

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso, Cursos) #modelo e modelo admin    

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)