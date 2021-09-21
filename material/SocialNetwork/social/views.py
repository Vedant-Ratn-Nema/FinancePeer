from django.shortcuts import render,redirect
from .forms import PostForm,CommentForm,ReplyForm
from datetime import datetime
from .models import Post,Comment,Reply
# Create your views here.

def add_post_view(request):
    context={}
    context['userinfo']=request.user
    if request.POST:
        form=PostForm(request.POST,request.FILES)
        obj=form.save(commit=False)
        obj.user=request.user
        obj.timestamp=datetime.now()
        print(obj)
        print(obj.timestamp)
        if form.is_valid():
            obj.save()
            return redirect('home')

        else:
            context['post_form']=form

    else:
        form=PostForm()
        context['post_form']=form
    return render(request,'social/add_post.html',context)



def home_view(request):
    context={}
    context['userinfo']=request.user
    context['post']=Post.objects.all().order_by('-timestamp')
    context['reply']=Reply.objects.all().order_by('-timestamp')
    context['comment']=Comment.objects.all().order_by('-timestamp')

    return render(request,'social/home.html',context)

def add_comment_view(request,id):
    context={}
    context['userinfo']=request.user

    if request.POST:
        print("ss")
        form=CommentForm(request.POST)
        if form.is_valid():
            print(form)
            trn=datetime.now()
            print(trn)
            obj=Comment.objects.create(post=(Post.objects.get(id=id)),comment_text=form.cleaned_data['comment_text'],timestamp=trn)
            obj.save()
            return redirect('home')

        else:
            context["comment_form"]=form

    else:
        form=CommentForm()
        context['comment_form']=form
    return render(request,'social/add_comment.html',context)

def add_reply_view(request,id):
    context={}
    context['userinfo']=request.user
    if request.POST:
        form=ReplyForm(request.POST)
        if form.is_valid():
            print(form)
            trn=datetime.now()
            print(trn)
            obj=Reply.objects.create(comment=(Comment.objects.get(id=id)),reply_text=form.cleaned_data['reply_text'],timestamp=trn)
            obj.save()
            return redirect('home')

        else:
            context["reply_form"]=form

    else:
        form=ReplyForm()
        context['reply_form']=form
    return render(request,'social/add_reply.html',context)



def comment():

    return 0

def reply():

    return 0
