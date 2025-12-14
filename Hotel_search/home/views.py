from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def Home(request):
    hotel_data = data.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'asc':
        hotel_data = hotel_data.order_by('hotel_price')
    elif sort_by == 'desc':
        hotel_data = hotel_data.order_by('-hotel_price')    
      
    context = {
        "all_data":hotel_data
    }
    return render(request,"home.html",context)


