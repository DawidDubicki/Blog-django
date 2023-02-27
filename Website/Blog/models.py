from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(max_length=100)
    likes = models.ManyToManyField(User, related_name='likes')


class AccountLikes(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by')
    liked_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_account')
    date = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')


class CommentsAnswer(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comments_answer_likes')


class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    date = models.DateTimeField(auto_now_add=True)


class FriendRequests(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_friend')
    date = models.DateTimeField(auto_now_add=True)


class Observer(models.Model):
    observer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observer')
    observed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observed')
    date = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_choices = [('M', 'Mężczyzna'), ('K', 'Kobieta')]
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=20, blank=True)
    description = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    profile_picture = models.ImageField()
