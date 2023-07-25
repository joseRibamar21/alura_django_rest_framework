from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento') # Campos que serão exibidos na listagem
    list_display_links = ('id', 'nome') # Campos que serão exibidos como links para alterar
    search_fields = ('nome',) # Campos que serão pesquisados
    list_per_page = 20 # Quantidade de registros por página

admin.site.register(Aluno, Alunos) # Registra o modelo Aluno e a Classe admin do mesmo

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel') 
    list_display_links = ('id', 'codigo_curso') 
    search_fields = ('codigo_curso',) 
    list_per_page = 20 

admin.site.register(Curso, Cursos) 
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo') 
    list_display_links = ('id',) 
    search_fields = ('aluno', 'curso') 
    list_per_page = 20

admin.site.register(Matricula, Matriculas)