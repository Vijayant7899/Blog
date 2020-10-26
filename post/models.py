from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Post(models.Model):
	sno = models.AutoField(primary_key=True)
	user = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	content = models.TextField()
	author = models.CharField(max_length=20)
	slug = models.CharField(max_length=300)
	likes = models.ManyToManyField(User,default=None,blank=True,related_name='likes')
	timestamp = models.DateTimeField(blank=True)

	def __str__(self):
		return self.title + 'by ' + self.author
	def num_likes(self):
		return self.likes.all().count()

	def get_like_url(self):
		return reverse("post:like-toggle",kwargs={"slug":self.slug})
	
	class BlogComment(models.Model):
	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)
	timestamp = models.DateTimeField(default=now)

	def _str_(self):
		return self.comment + 'by ' + self.user.username

