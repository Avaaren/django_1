from django.urls import path
from .views import index, by_rubric, BbCreateView

urlpatterns = [
path('', index, name = 'index'),
path('<int:rubric_id>/', by_rubric, name = 'by_rubric'), #url параметр который передается в функцию
path('add/', BbCreateView.as_view(), name = 'add'),
]