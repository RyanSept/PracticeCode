from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$",views.todo_home, name="todo_home"),
    url(r"^(?P<pk>[0-9]+)/edit/$", views.edit_task,name="edit"),
    url(r"^create/$",views.create_task,name="create"),
    url(r"^(?P<pk>[0-9]+)/delete/$", views.delete, name="delete"),
    ]
