# from django.db import models
# # from django.contrib.auth.models import User, Group 
# # class Musician(models.Model):
# # 	first_name = models.CharField(max_length=30)
# # 	last_name = models.CharField(max_length=30)
# # 	instrumnet = models.CharField(max_length=100)

# # class Album(models.Model):
# # 	artist = models.ForeignKey(Musician)
# # 	name = models.CharField(max_length=100)
# # 	release_date = models.DateField(auto_now=False, auto_now_add=False)	
	

# # Create your models here.
# # class MyUser(models.Model):
# #     user = models.OneToOneField(User)
# #     city = models.CharField(max_length=50, blank=False, default='Hyderabad')
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)


# class User(models.Model):
# 	username = models.CharField(max_length=10)
# 	password = models.CharField(max_length=20)
# 	email = models.CharField(max_length=25)
# 	dt = models.DateTimeField(auto_now=False, auto_now_add=False,)
# 	def __str__(self):
# 		return self.username
#               # __unicode__ on Python 2
        
class Following(models.Model):
	follower = models.ForeignKey(User)
	followee = models.ForeignKey(User , related_name='x')
	dt = models.DateTimeField(auto_now=False, auto_now_add=False)


class Photo(models.Model):
	picture = models.BinaryField()
	dt = models.DateTimeField(auto_now=False, auto_now_add=False)
	user = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now=False, auto_now_add=False)
    text = models.TextField()
    mentioned = models.ManyToManyField(User,related_name='add_users')

    def __str__(self):
    	return self.text    

class Like(models.Model):
	user = models.ForeignKey(User)
	photo = models.ForeignKey(Photo,related_name='likedphots')
	dt = models.DateTimeField(auto_now=False, auto_now_add=False)











	# photos = models.ManyToManyField(Photo)

# from django.db import models

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):              # __unicode__ on Python 2
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()

#     def __str__(self):              # __unicode__ on Python 2
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

#     def __str__(self):              # __unicode__ on Python 2
#         return self.headline