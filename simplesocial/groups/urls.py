from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroup.as_view(), name='all'),
    path('new', views.CreateGroupView.as_view(), name='create'),
    path('posts/in/<str:slug>', views.SingleGroup.as_view(), name='single'),
]