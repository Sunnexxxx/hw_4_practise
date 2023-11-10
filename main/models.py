from django.db import models


class Json(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField()

    def __str__(self):
        return self.title

