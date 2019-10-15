from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb, Rubric

def index(request):
	bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	context = {'bbs':bbs, 'rubrics': rubrics}
	return render(request, 'bboard/index.html', context)#Параметры передаваемые в шаблон

def by_rubric(request, rubric_id): #Получает значение из урл параметра который мы передаем в адрес
	bbs = Bb.objects.filter(rubric = rubric_id) #плучить объекты где поле rubric = rubric id (2) идет сортировка по индексу
	rubrics = Rubric.objects.all()#
	current_rubric = Rubric.objects.get(pk = rubric_id)#получить объекты где первичный ключ = rubric id
	context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}#параметры передаваемые в шаблон
	return render (request, 'bboard/by_rubric.html', context)

# Create your views here.
