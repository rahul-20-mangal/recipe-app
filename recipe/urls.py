from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('<int:pk>/', views.recipe_detail, name='detail'),
]