from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic import RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin

def imageUpload(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.user = request.user;
			obj.save()
		return redirect("blogHome")
	else:
		form = ProfileForm()
	return render(request, 'imageUpload.html', {'form' : form})

		

def blogHome(request):
	post = Post.objects.all()
	context = {'post' : post}
	return render(request,'blogHome.html', context)
	

def blogPost(request, slug):
	post = Post.objects.filter(slug = slug).first()
	comments = BlogComment.objects.filter(post=post)
	imageobj = Profile.objects.all()
	l = Like.objects.filter(post=post)
	context = {'post' : post,'comments':comments,'imageobj':imageobj}
	return render(request,'blogPost.html', context)

def postComment(request):
	if request.method=="POST":
		comment = request.POST.get("comment")
		postSno = request.POST.get("postSno")
		user = request.user
		post = Post.objects.get(sno=postSno)
		comment = BlogComment(comment=comment,user=user,post=post)
		comment.save()
		messages.success(request,"success")
	return redirect(f"/post/{post.slug}")

#to implement like/dislike on post

def delete_com(request):
	user = request.user.id
	comment_id = request.POST.get("c_id")
	post_id = request.POST.get("post_id")
	userid = request.POST.get("userid")
	userid = int(userid)
	post_obj = Post.objects.get(sno=post_id)
	if request.method == "POST":
		if user == userid:
			obj = BlogComment.objects.get(sno=comment_id,user_id=user)
			obj.delete()
		else:
			messages.success(request,"cant delete")
			return redirect(f"/post/{post_obj.slug}")

	return redirect(f"/post/{post_obj.slug}")

def myPost(request):
	return render(request,'myPost.html')