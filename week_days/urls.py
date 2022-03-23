from django.urls import path
from . import views

urlpatterns = [
    path('<int:which_day>/', views.get_info_abou_week_day_number),
    path('<str:which_day>/', views.get_info_about_week_day)
]