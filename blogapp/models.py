from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()
    title = models.CharField(max_length=200)
    time = models.DateTimeField("Published Date", blank=True)
    slug = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title + " by " + self.author

class CommentModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment_text = models.TextField()
    blog = models.ForeignKey('Blog', on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name