from django.db import models
from django.contrib.auth.models import User

RATING_CHOICES = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='articles', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} - {self.created_at}"


class Rating(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('blog', 'user')
    
    def __str__(self) -> str:
        return f"{self.blog.title} - Rating: {self.rating}"