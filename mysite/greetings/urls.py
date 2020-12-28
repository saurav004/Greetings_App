from django.urls import path
from .views import HomeView, DetailedView, AddView, EditView, RemoveView, GreetingList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', HomeView.as_view(), name='greetings_home'),
    path('api', GreetingList.as_view(), name="greetings_api"),
    path('addGreeting', AddView.as_view(), name='greetings_add'),
    path('greeting/<int:pk>', DetailedView.as_view(), name='SingleGreeting'),
    path('greeting/edit/<int:pk>', EditView.as_view(), name='edit_Greeting'),
    path('greeting/delete/<int:pk>', RemoveView.as_view(), name='delete_Greeting'),
]
