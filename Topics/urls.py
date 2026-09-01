from django.urls import path
from . import views

urlpatterns=[
    path('',views.alltopics,name="alltopics"),
    path('add/',views.add),
    path('update/<str:topic_id>',views.update,name="update"),
    path('searchupdate/',views.searchupdate),
    path('searchdelete/',views.searchdelete),
    path('delete/<str:topic_id>',views.delete,name="delete"),
    path('confirm/<str:topic_id>',views.confirm),
    path('maindelete/<str:topic_id>',views.maindelete,name="maindelete"),
    path('searchtopic/',views.searchtopic),
    path('singletopic/<str:topic_name>',views.singletopic,name="singletopic"),
]