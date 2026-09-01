from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="allsubjects"),
    path('add/',views.add),
    path('searchupdate/',views.searchupdate),
    path('update/<str:sub_name>',views.update,name="update"),
    path('searchdelete/',views.searchdelete),
    path('searchsinglesub/',views.searchsinglesub),
    path('delete/<str:sub_name>',views.delete,name="delete"),
    path('confirm/<str:sub_name>',views.confirm),
    path('maindelete/<str:sub_name>',views.maindelete,name="maindelete"),
    path('singlesub/<str:sub_name>',views.singlesub,name="singlesub"),

]