from django.urls import path
from .views import *


urlpatterns = [
    path('',index),
    path('save/',save,name="save"),
    path('delete/',delete,name="delete"),
]
