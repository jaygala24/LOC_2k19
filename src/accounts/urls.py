from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('members/', views.members_data, name='members'),
    path('volunteers/', views.volunteers_data, name='volunteers'),
    path('donors/', views.donors_data, name='donors'),
    path('volunteers/change/<int:pk>/',
         views.volunteer_change_view, name='change'),
]
