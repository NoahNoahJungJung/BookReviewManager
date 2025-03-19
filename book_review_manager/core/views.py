from django.shortcuts import render
from django.http import JsonResponse

def init_view(request):
    return JsonResponse({"message": "This is my first endpoint!"})

def project_info(request):
    return JsonResponse({"project_info": "This app manages your book reviews. It is for my personal study. "})