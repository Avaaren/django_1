from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BbForm

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
class BbCreateView(CreateView):
	template_name = 'bboard/create.html'#путь к файлу шаблона что будет использован для вывода страницы с формой
	form_class = BbForm#класс формы 
	success_url = reverse_lazy('index')
	#'/bboard/'#Адресс куда будет перенаправление после успешнго сохранения данных
	#Принимает имя маршрута и значение url параметров, рез-т - готовый адрес
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context
		# Мы получаем от CreateView базовый контекст,
		# который мы мы объявили в теле класса, 
		# потом мы добавляем к нему список рубрик,
		# так как контекст - это словарь,
		# и возвращаем уже целостный 