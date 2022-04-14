from django.urls import path
from . import views

urlpatterns = [
    path('produtos', views.ProdutoList.as_view()),

]