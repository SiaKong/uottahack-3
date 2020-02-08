from django.shortcuts import render
from django.http import HttpResponse
from .models import MapGroup, User

#First view - index, contains the interactive map
def index(request):
	return HttpResponse("Hello, world")

#View a given group and its members
def view_group(request, group_id):
	group = MapGroup.objects.get(id=group_id)
	context = {
		'group' : group,
		'group_id' : group_id
	}
	return render(request, 'map/view_group.html', context)

#View all your user's friends, and all the groups you're a part of
def view_user(request, user_id):
	user = User.objects.get(id=user_id)
	context = {
		'user' : user,
		'user_id' : user_id
	}
	return render(request, 'map/view_user.html', context)

#Create a new user
def create_user(request):
	context = {}
	return render(request, 'map/create_user.html', context)

#Create a new group
def create_group(request):
	context = {}
	return render(request, 'map/create_group.html', context)

