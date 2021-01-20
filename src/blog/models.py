from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    OPTIONS = (
        ("d", "Draft"),
        ("p", "Published")
    )

    title = models.CharField(max_length=100, verbose_name="Post Title")
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default="d")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
