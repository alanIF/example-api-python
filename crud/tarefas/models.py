from django.db import models


class Tarefa(models.Model):
    nome= models.CharField(max_length=200)
    
