from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GreetingClass

# rest api imports
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GreetingClassSerializer


class HomeView(ListView):
    model = GreetingClass
    template_name = 'Home.html'
    ordering = ['-id']


class DetailedView(DetailView):
    model = GreetingClass
    template_name = 'SingleGreeting.html'


class AddView(CreateView):
    model = GreetingClass
    template_name = 'addGreeting.html'
    fields = '__all__'


class EditView(UpdateView):
    model = GreetingClass
    template_name = 'edit_greeting.html'
    fields = ['Greeting_Title', 'message']


class RemoveView(DeleteView):
    model = GreetingClass
    template_name = 'delete_post.html'
    fields = ['Greeting_Title', 'message']
    success_url = reverse_lazy('greetings_home')


class GreetingList(APIView):

    def get(self, request):
        greeting_objects = GreetingClass.objects.all()
        serializer = GreetingClassSerializer(greeting_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return HttpResponse('<h1> dashboard</h1>')


def add_greeting(request):
    return HttpResponse('<h1> add greeting</h1>')


def edit_greeting(request):
    return HttpResponse('<h1> edit greeting </h1>')


def sign_up(request):
    return HttpResponse('<h1>sign_up </h1>')


def logout(request):
    return HttpResponse('<h1> logout  </h1>')
