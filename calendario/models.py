from django.db import models

class Entry(models.Model): #classes
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): #mostrar como será exibido na pagina do admin ou quando for referenciado
        return f'{self.name} {self.date}'
