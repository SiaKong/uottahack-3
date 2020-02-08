from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#A model that adds some extra fields to the default User object.
class MapUser(models.Model):
	#The user associated with this MapUser. OneToOneField makes them
	#automatically associated with one another.
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#Additional data:
	#'self' indicates that if this user is friends with another user,
	#then both are automatically part of each other's friends list.
	friends = models.ManyToManyField('self')

#Whenever a user is created, a corresponding MapUser objects is created.
#Always.
@receiver(post_save, sender=User)
def create_mapuser(sender, instance, created, **kwargs):
	if created:
		MapUser.objects.create(user=instance)

#Similarly, whenever a user is saved, their corresponding MapUser is saved
#and vice versa.
@receiver(post_save, sender=User)
def save_mapuser(sender, instance, **kwargs):
	#may be an issue; might be mapUser?
	instance.mapuser.save()





'''
class User(models.Model):
	#id = models.IntegerField(primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	friends = models.ManyToManyField('self')

	def __str__(self):
		return f"User {self.username}#{self.id}"
'''
class MapGroup(models.Model):
	#id = models.IntegerField(primary_key=True)
	groupname = models.CharField(max_length=30)
	users = models.ManyToManyField(User)

	def __str__(self):
		return f"Group {self.groupname}#{self.id}"


