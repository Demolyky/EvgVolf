from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
week_day_dict = {
    'monday': "Понедельник",
    'tuesday': "Вторник",
    'wednesday': "Среда",
    'thursday': "Четверг",
    'friday': "Пятница",
    'saturday': "Суббота",
    'sunday': "Воскресенье"
}

def get_info_about_week_day(request, which_day: str):
    day = week_day_dict.get(which_day, None)
    if day:
        return HttpResponse(f'Это - {day}')
    else:
        return HttpResponseNotFound(f'{which_day} - это не день недели')

def get_info_abou_week_day_number(request, which_day: int):
    week_day_numbers = list(week_day_dict)
    if not 0 < which_day < len(week_day_numbers):
        return HttpResponseNotFound(f'Неверный номер дня - {which_day}')
    name_week_days = week_day_numbers[which_day-1]
    return HttpResponseRedirect(f'/todo_week/{name_week_days}')
        