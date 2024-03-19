from django.db import models

class Bolsistas(models.Model):
    matricula = models.CharField(max_length=14)

    def __str__(self):
        return self.matricula