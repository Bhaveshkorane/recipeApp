from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.recipies,name='recipe_url'),
    path('show/',views.show_recipe,name='show_url'),
    path('delete/<id>/',views.delete_recipe,name='delete_url'),
     path('update/<id>/',views.update_recipe,name='update_url')
]
