from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

zodiac_dict = {
    'aries': "Aries [ˈɛəriːz] — Овен",
    'taurus': "Taurus [ˈtɔːrəs] — Телец",
    'gemini': "Gemini [ˈʤemɪnaɪ] — Близнецы",
    'cancer': "Cancer [ˈkænsə] — Рак",
    'leo': "Leo [ˈliːəʊ] — Лев",
    'vigro': "Virgo [ˈvɜːgəʊ] — Дева",
    'libra': "Libra [ˈlɪ:brə] — Весы",
    'scorpio': "Scorpio [ˈskɔːpɪəʊ] — Скорпион",
    'sagittarius': "Sagittarius [sæʤɪˈtɛərɪəs] — Стрелец",
    'capricorn': "Capricorn [ˈkæprɪkɔːn] — Козерог",
    'aquarius': 'Aquarius [əˈkwɛərɪəs] — Водолей',
    'pisces': 'Pisces [ˈpaɪsiːz] — Рыбы'
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")


def get_info_about_sign_zodiac_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Не существует такого знака зодиака')
    name_zodiac = zodiacs[sign_zodiac-1]
    return HttpResponseRedirect(f'/horoscope/{name_zodiac}')