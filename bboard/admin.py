from django.contrib import admin

from .models import Bb
from .models import Rubric

class BbAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published', 'rubric')
	#Последовательность имен полей, которые должны выводиться в списке записей
	list_display_links = ('title', 'content')
	#Последовательность имен полей которые должны быть
	#преобразованы в гиперссылки ведущие на страницу правки
	search_fields = ('title', 'content',)
	#Последовательность имен полей по которым должна выполняться фильлтрация

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)

# Register your models here.
