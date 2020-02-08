from django.urls import path

from . import views

app_name = 'map'

urlpatterns = [
	path('', views.index, name='index'),
	path('users/<int:user_id>', views.view_user, name='view_user'),
	path('groups/<int:group_id>', views.view_group, name='view_group'),
	path('create_user', views.create_user, name='new_user'),
	path('create_group', views.create_group, name='new_group'),
]