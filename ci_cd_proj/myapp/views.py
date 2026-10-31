from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")
def about(request):
    return HttpResponse("<h1>About Page</h1>")

@api_view(['GET'])
def api_hello(request):
    return Response({"message": "Hello, World!", "status": "success"})