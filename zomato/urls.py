from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('load_data/', views.load_data, name='load_data'),
    path('filter_data/', views.filter_data, name='filter_data'),
    path('about/', views.about, name='about'),
    path('index/', views.home, name='home'),
    path('heatmap', views.heatmap, name="heatmap"),
    path('Zomato', views.Zomato, name="Zomato"),
    path('get_info/<int:ind>/', views.get_info, name='get_info'),
    path('testing/', views.testing, name='testing'),

]
