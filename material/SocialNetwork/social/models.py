from django.db import models

# Create your models here.
class Post(models.Model):
    user        =models.ForeignKey('Account.UserAccount',on_delete=models.CASCADE)
    image       =models.ImageField(upload_to='post_pictures')
    caption     =models.TextField(null=True,blank=True)
    timestamp   =models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    post             =models.ForeignKey('social.Post',on_delete=models.CASCADE)
    comment_text     =models.TextField()
    timestamp        =models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    comment          =models.ForeignKey('social.Comment',on_delete=models.CASCADE)
    reply_text       =models.TextField()
    timestamp        =models.DateTimeField(auto_now_add=True)
