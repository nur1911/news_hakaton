from django.urls import path

from newsapp import views
from .views import news_list


urlpatterns = [
    path('all/',views.news_list),
    path('detail/<int:pk>/',views.news_detail),

]

