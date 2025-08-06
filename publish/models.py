from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model



User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Created Date", default=timezone.now)
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(verbose_name="Content")
    slug = models.SlugField(verbose_name="Slug")
    view_count = models.IntegerField(verbose_name="View Count", default=0)
    
    def get_absolute_url(self):
        return reverse("view_post", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    