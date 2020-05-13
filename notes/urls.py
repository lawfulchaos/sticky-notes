from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_details, name='note_details'),
    path('note/new/', views.note_new, name='note_new'),
]