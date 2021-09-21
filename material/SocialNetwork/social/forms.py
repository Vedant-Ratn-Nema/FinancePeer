from django import forms
from Account.models import UserAccount
from .models import Post,Comment,Reply


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image','caption']

class CommentForm(forms.Form):
    comment_text=forms.CharField(help_text='Enter the comment',required=True)

class ReplyForm(forms.Form):
    reply_text=forms.CharField(help_text='Enter the comment',required=True)
