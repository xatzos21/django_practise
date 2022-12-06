from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def hello_json(request):
    dict = {"name": "dimi", "surname": "aek"}
    return JsonResponse(dict)