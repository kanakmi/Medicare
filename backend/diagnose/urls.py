from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='dashboard'),
    path('diagnose',diagnose),
    path('diagnose/diabetes',diabetesr),
    path('diagnose/thyroid',thyroism),
    path('diagnose/heart',heartdis),
    path('social',social_help),
    path('diagnose/covid',covid_classifier),
    path('diagnose/brain',brain)
]