from django.contrib import admin

from mi_app.models import *
from mi_app.models import Alumno, Curso, Matricula

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(Document)