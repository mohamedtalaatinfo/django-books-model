from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Books(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=250)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    slug = models.SlugField()
    author = models.ForeignKey(Author, models.SET_NULL, null=True , related_name='books')
    published_countries = models.ManyToManyField(Country)


    def __str__(self):
        return f"{self.title} -- {self.author}"
