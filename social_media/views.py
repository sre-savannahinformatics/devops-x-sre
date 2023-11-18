from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class CreatePostView(View):
    def get(self, request):
        return render(request, 'create_post.html')

    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect('home')

class ViewPostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post__id=post.id)
        return render(request, 'view_post.html', {'post': post, 'comments': comments})

class CommentOnPostView(View):
    def get(self, request, post_id):
        return render(request, 'comment_on_post.html')

    def post(self, request, post_id):
        content = request.POST['content']
        post = Post.objects.get(id=post_id)
        Comment.objects.create(content=content, author=request.user, post__id=post.id)
        return redirect('view_post', post_id=post_id)

class AllPostsView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'all_posts.html', {'posts': posts})

