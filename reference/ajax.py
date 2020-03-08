from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Проверяем форму ввода страны каждый раз когда она редактируется и выдаем отфильтрованные страны
def check_country_form(request):
    form = request.POST
    query = find_query(delete_empty(form))
    countryes = Country.objects.raw(query)
    print(countryes)
    return HttpResponse(countryes)

# Доп функции.
def delete_empty(enter_dict):
    dict = enter_dict.copy()
    for key in list(dict):
        if len(str(dict[key])) < 1:
            value = dict.pop(key)
    return dict


def find_query(dict):
    string = "SELECT * FROM reference_country WHERE "
    for key in list(dict):
        string += key + "='" + dict[key] + "', "
    return string[:-2]

# **********************************************************************


# Создание новой страны
def create_new_country(request):
    form = request.POST

    country = Country()

    country.country_id = form["country_id"]
    country.country_class = form["country_class"]
    country.code = form["code"]
    country.name = form["name"]
    country.ondate = form["ondate"]
    country.offdate = form["offdate"]
    country.issystem = form["issystem"]
    country.basison = form["basison"]
    country.basisoff = form["basisoff"]
    country.short = form["short"]
    country.alpha2 = form["alpha2"]
    country.alpha3 = form["alpha3"]
    country.en = form["en"]
    country.updated = form["updated"]

    country.save()
    return HttpResponse({"result": "True"})


# ***************************************************************************


# Проверяем форму ввода типа платежа каждый раз когда она редактируется и выдаем отфильтрованные страны
def check_payment_form(request):
    form = request.POST
    query = find_query(delete_empty(form))
    print(query)
    # payment = Country.objects.raw(query)
    # print(countryes)
    return HttpResponse('<div class="alert alert-primary" role="alert">Test complete!</div>')


# Создание нового типа платежа
def create_new_payment(request):
    return HttpResponse({"result": "True"})