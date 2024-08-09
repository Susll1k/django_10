from django.shortcuts import render
from django.http import JsonResponse
import json


def home(request):
    list = [i for i in range(1,10)]
    return JsonResponse(list, safe=False)