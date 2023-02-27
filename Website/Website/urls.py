"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog.views import main_view, account_view, login_view, register_view, post_like, search_user, post_comment
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_url'),
    path('profile/<username>', account_view, name='account_url'),
    path('login', login_view, name='login_url'),
    path('register', register_view, name='register_url'),
    path('post-like', post_like, name='post_like_url'),
    path('user-search', search_user, name='search_user_url'),
    path('post-comment', post_comment, name='post_comment_url')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
