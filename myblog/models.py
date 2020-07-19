from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    topic = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.topic
