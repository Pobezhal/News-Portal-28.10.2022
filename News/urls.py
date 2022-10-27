from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [

   path('', PostList.as_view(), name= 'post_list'),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('create/', PostCreate.as_view(), name = 'post_create'),

]


