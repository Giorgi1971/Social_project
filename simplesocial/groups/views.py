from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                            PermissionRequiredMixin,
                                                )

from django.urls import resolve
from django.views import generic
from groups.models import Group, GroupMember

class CreateGroupView(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DeleteView):
    model = Group

class ListGroup(generic.ListView):
    model = Group
