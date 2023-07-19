from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=30)
    head = models.CharField(max_length=30)
    text = models.TextField()
    page_layk = models.IntegerField()


    def __str__(self):
        return f"{self.id} - {self.author}"

    def get_absolute_url(self):
        return f"/{self.pk}"

