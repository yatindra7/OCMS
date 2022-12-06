from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search_view, name='search')
    # path('privatecomment/create/<int:assignment_pk>/', views.create_private_comment, name='private_comment'),
]
