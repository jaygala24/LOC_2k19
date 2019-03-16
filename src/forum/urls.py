from django.urls import path
from .views import post_create, post_detail, post_list

app_name = 'forum'

urlpatterns = [
    path('', post_list, name='list'),
    path('<int:pk>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
]
