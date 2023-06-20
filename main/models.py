from django.db import models

# Create your models here.
""" after edit/update then run (python manage.py makemigrations main) to include
new update and run (python manage.py migrate to build) """
"""
	run (python manage.py shell) to acccess data (32:30)
"""
class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text

class contactForm(models.Model):
	username = models.CharField(max_length = 30)
	email = models.EmailField()
	body = models.TextField()

	def __str__(self):
		return self.username

""" get data from database """
class postForm(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

class upForm(models.Model):
	title = models.CharField(max_length=255)
	image = models.FileField()
	body = models.TextField()

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=30)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class upMulti(models.Model):
	image = models.FileField()

#API
class Food(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.name




