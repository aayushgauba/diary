from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_list, name='diary_list'),
    path('new/', views.diary_create, name='diary_create'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('entries/json/', views.diary_entries_json, name='diary_entries_json'),
    path('entry/<int:id>/', views.diary_detail, name='diary_detail'),
]