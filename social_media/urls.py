from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CreatePostView, ViewPostView, CommentOnPostView, AllPostsView

urlpatterns = [
    path('home/', AllPostsView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('view_post/<int:post_id>/', ViewPostView.as_view(), name='view_post'),
    path('comment_on_post/<int:post_id>/', CommentOnPostView.as_view(), name='comment_on_post'),
]
