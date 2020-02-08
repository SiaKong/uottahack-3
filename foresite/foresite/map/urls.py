from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('users/<int:user_id>', views.view_user, name='user'),
	path('groups/<int:group_id>', views.view_group, name='group'),
	path('create_user', views.create_user, name='new_user'),
	path('create_group', views.create_group, name='new_group'),
]