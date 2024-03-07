from django.db import models

"""Creation of The related Models"""


class Category(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE, null=True)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True, default='covers/OIG3.jpeg')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"The Author: {self.author} commented on {self.post}"
