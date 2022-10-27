from django_filters import FilterSet, ModelChoiceFilter
from .models import *


class PostFilter(FilterSet):
   categoria = ModelChoiceFilter(
       field_name = 'category',
       queryset = Category.objects.all(),
       label = 'Категория',
       empty_label = 'Любая',)

   Avtor = ModelChoiceFilter(
        field_name = 'author_id',
        queryset = Author.objects.all(),
        label = 'Автор',
        empty_label = 'Все писаки',)



   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
           'post_time' : ['gt']
      }



