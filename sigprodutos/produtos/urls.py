from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('new', views.new, name='new'),
    path('store', views.store, name='store'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/', views.update, name='update'),

]