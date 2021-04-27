from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('<int:pk>/', views.recipe_detail, name='detail'),
    path('add', views.add_recipe, name="add"),
    path('edit/<int:pk>/', views.edit_recipe, name='edit'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete'),
    path('create_collection/', views.create_collection, name='create-collection'),
    path('my_collection/', views.my_collection, name='my-collection'),
]