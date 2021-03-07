
from django.urls import path
from . import  views

urlpatterns = [
    path('postget/', views.postGet),
    path('postget/<int:id>', views.postGet)
]