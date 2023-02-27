from django.shortcuts import render
from .forms import LoginForm, RegisterForm, AddPostForm
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
import json
# Create your views here.


def main_view(request):
    context = {}
    posts = Post.objects.all().order_by('-date')
    if request.user.is_authenticated:
        form = AddPostForm()
        context['form'] = form
        if request.method == 'POST':
            if request.POST.get('logout') == 'True' and User.is_authenticated:
                logout(request)
            elif User.is_authenticated:
                form = AddPostForm(request.POST)
                context['form'] = form
                if form.is_valid():
                    title = form.cleaned_data['title']
                    text = form.cleaned_data['text']
                    tags = form.cleaned_data['tags']
                    post = Post(user=request.user, text=text, tags=tags, title=title)
                    post.save()
                    return redirect('main_url')
        else:
            if request.GET.get('search'):
                query = request.GET.get('search')
                posts = Post.objects.filter(title__contains=query).order_by('-date')
    context['posts'] = posts
    friend_list = Friends.objects.filter(user=request.user.id)
    if friend_list.exists():
        context['friends'] = friend_list
    return render(request,'main.html', context)


def account_view(request, username):
    observed_by_count = Observer.objects.filter(observed=request.user.id).count()
    observed_count = Observer.objects.filter(observer=request.user.id).count()
    account_likes_count = AccountLikes.objects.filter(liked_account=request.user.id).count()
    user = get_object_or_404(User, username=username)
    friend_list = Friends.objects.filter(user=request.user.id)
    posts = Post.objects.filter(user=user.id)
    context = {'user': user, 'observed_by_count': observed_by_count, 'observed_count': observed_count,
               'account_likes_count': account_likes_count, 'friend_list': friend_list,'posts': posts,}
    if request.user.is_authenticated and request.user.username == username:
        pass

    return render(request, 'account.html', context)


def login_view(request):
    form = LoginForm()
    context = {'form': form,}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user=user)
                return redirect('main_url')
    return render(request, 'login.html', context)


def register_view(request):
    form = RegisterForm
    context = {'form': form,}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            user = User.objects.filter(username=username)
            if password == password_repeat and not user:
                user = User.objects.create_user(username=username, password=password)
                login(request, user=user)
                return redirect('main_url')
    return render(request, 'register.html', context)


def post_like(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.body:
                user = request.user
                data = json.loads(request.body)
                if Post.objects.filter(likes=user.id, id=data['post_id']):
                    post = Post.objects.get(id=data['post_id'])
                    post.likes.remove(user.id)
                    return HttpResponse(status=200)
                else:
                    post = Post.objects.get(id=data['post_id'])
                    post.likes.add(user)
                    post.save()
                    return HttpResponse(status=201)
        else:
            return HttpResponse(status=401)


def post_comment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.body:
                user = request.user
                data = json.loads(request.body)
                print (data)
                if Post.objects.get(id=data['post_id']):
                    post = Post.objects.get(id=data['post_id'])
                    if Comments.objects.filter(post=post, user=user).count() < 6:
                        comment = Comments(post=post, user=user, text=data['comment_text'])
                        comment.save()
                        return render(request, 'single_comment.html', {'comment': comment})
                    else:
                        return HttpResponse(status=403)


def search_user(request):
    context = {}
    if request.GET.get('search'):
        query = request.GET.get('search')
        users = User.objects.filter(username__contains=query)
        context['users'] = users
    return render(request, 'user-search.html', context)
