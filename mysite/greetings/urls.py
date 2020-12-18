from django.urls import path

from . import views
from .views import HomeView, DetailedView, AddView, EditView, RemoveView, GreetingList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', HomeView.as_view(), name='greetings_home'),
    path('api', GreetingList.as_view(), name="greetings_api"),
    path('addGreeting', AddView.as_view(), name='greetings_add'),
    path('greeting/<int:pk>', DetailedView.as_view(), name='SingleGreeting'),
    path('greeting/edit/<int:pk>', EditView.as_view(), name='edit_Greeting'),
    path('greeting/delete/<int:pk>', RemoveView.as_view(), name='delete_Greeting'),
    path('login', views.login, name='greetings_login'),
    path('signup', views.sign_up, name='greetings_sinup'),
    path('greetings/dashboard', views.dashboard, name='greetings_dashboard'),
    path('add', views.add_greeting, name='greetings_addGreeting'),
    path('edit', views.edit_greeting, name='greetings_edit'),
    path('logout', views.logout, name='greetings_logout'),
]
