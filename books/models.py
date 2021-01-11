from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64, null=True)
    authour = models.CharField(max_length=64, null=True)
    url = models.URLField(null=True)
    image = models.URLField(null=True, default="https://unmpress.com/sites/default/files/default_images/no_image_book.jpg")
    dsc = models.TextField(null=True)
    date = models.CharField(max_length=30, null=True)
    active = models.BooleanField(default=False)
    rank = models.IntegerField(null=True, default=0)

    def __str__(self):
        if self.active:
            state = "Active"
        else:
            state = "Inactive"

        return f"{self.title} by {self.authour}, ({state}, Rank: {self.rank})"

class ReadingList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="readinglist")
    books = models.ManyToManyField(Book)    

    def __str__(self):
        return f"{self.user}'s Reading List"

