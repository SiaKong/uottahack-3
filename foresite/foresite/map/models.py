from django.db import models

class User(models.Model):
	#id = models.IntegerField(primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	friends = models.ManyToManyField('self')

	def __str__(self):
		return f"User {self.username}#{self.id}"

class Group(models.Model):
	#id = models.IntegerField(primary_key=True)
	groupname = models.CharField(max_length=30)
	users = models.ManyToManyField(User)

	def __str__(self):
		return f"Group {self.groupname}#{self.id}"

