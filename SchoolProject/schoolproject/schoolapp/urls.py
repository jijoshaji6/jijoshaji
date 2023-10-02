
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('get_course/',views.get_course,name='get_course'),
]
