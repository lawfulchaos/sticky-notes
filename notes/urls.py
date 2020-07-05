from django.urls import path
from . import views

urlpatterns = [
    path('note/<int:pk>/', views.note_details, name='note_details'),
    path('note/new/', views.note_new, name='note_new'),
    path('note_secret', views.note_secret, name='note_secret'),
    path('', views.note_list, name='note_list'),
    path('user/<slug:user>/', views.note_by_author, name='note_by_author'),
]