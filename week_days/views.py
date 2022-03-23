from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
week_day_dict = {
    'monday': "Понедельник",
    'tuesday': "Вторник",
    'wednesday': "Среду",
    'thursday': "Четверг",
    'friday': "Пятницу",
    'saturday': "Субботу",
    'sunday': "Воскресенье"
}

def get_info_about_week_day(request, which_day: str):
    day = week_day_dict.get(which_day, None)
    if day:
        return HttpResponse(f'Это - {day}')
    else:
        return HttpResponseNotFound(f'{which_day} - это не день недели')

def get_info_abou_week_day_number(request, which_day: int):
    if 0 < which_day < 8:
        return HttpResponse(f'Сегодня {which_day} день недели')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {which_day}')