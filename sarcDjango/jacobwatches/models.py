from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    watch = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Watch(models.Model):
    watchcode = models.IntegerField()
    watchname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    perPrice = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.watchname
