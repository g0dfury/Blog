from django.db import models
from authe.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    