from django.db import models

# Create your models here.
class Bb(models.Model):
	title = models.CharField(max_length = 50, verbose_name = "Товар")
	content = models.TextField(null = True, blank = True, verbose_name = "Описание")
	price = models.FloatField(null = True, blank = True, verbose_name = "Цена")
	published = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name = "Опубликовано")
	rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = "Рубрика")
#В поле внешнего ключа фактически хранится ключ записи из первичной модели
	class Meta:
		verbose_name_plural = 'Объявления' #Название моедли во множественном числе
		verbose_name = 'Объявление' #Название модели в единственном числе	
		ordering = ['-published']
class Rubric(models.Model):
	name = models.CharField(max_length = 20, db_index = True, verbose_name = "Рубрики")

	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name_plural = 'Рубрики' #Название моедли во множественном числе
		verbose_name = 'Рубрика' #Название модели в единственном числе	
		ordering = ['-name'] 