import math
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def get_calculate_geometry(request, calculate_geometry):
    return HttpResponse('ggwp')

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника = {width * height}')

def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата = {width**2}')

def get_circle_area(reauest, radius: int):
    return HttpResponse('Площадь круга = {:.1f}'.format(math.pi*radius**2))