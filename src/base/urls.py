from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('room/', views.room, name='room'),
    path('get_token/', views.getToken, name='getToken'),

    path('create_member/', views.createMember, name='createMember'),
    path('get_member/', views.getMember, name='getMember'),
    path('delete_member/', views.deleteMember, name='deleteMember'),
]
