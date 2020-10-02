from django.urls import path
from . import views
# from .views import PostLikeToggle
# from django.contrib.auth import views as as_views

urlpatterns = [
	path('postComment',views.postComment,name='postComment'),
	path('imageUpload',views.imageUpload,name='imageUpload'),
	path('',views.blogHome,name='blogHome'),
	path('myPost',views.myPost,name='myPost'),
	path('like',views.like_post,name='like-post'),
	path('delete',views.delete_com,name='delete_com'),
	path('<str:slug>',views.blogPost,name='blogPost'),

	
	

	
]