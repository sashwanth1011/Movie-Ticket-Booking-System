from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    show_time = models.CharField(max_length=20)
    ticket_price = models.IntegerField()
    available_seats = models.IntegerField(default=50)

    def __str__(self):
        return self.name

    