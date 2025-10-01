from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=50)
    content = models.TextField("글 내용")
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField("댓글 내용")
    
    def __str__(self):
        return f"{self.post.title}의 댓글 (ID:{self.id})"