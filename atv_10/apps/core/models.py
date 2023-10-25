from django.db import models

class Label(models.Model):
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name

class Discs(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição", max_length=400)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    year = models.PositiveIntegerField("Ano", default=2023)
    country = models.CharField("País", max_length=100)
    gender = models.CharField("Genero", max_length=50)
    qtd = models.PositiveIntegerField("Quantidade", default=0)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField("Nome", max_length=50)
    disc = models.ManyToManyField(Discs)

    def __str__(self):
        return self.name