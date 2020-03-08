from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def main(request):
    return render(request, "base_template.html")


def payments_reference(request):
    return render(request, "forms/reference_payment.html")


def country_reference(request):
    countryes = Country.objects.all()
    return render(request, "forms/reference_country.html", locals())


def add_payment(request):
    return render(request, "forms/add_payment.html")


def add_country(request):
    return render(request, "forms/add_country.html")


def excel_adder(request):
    return render(request, "forms/excel_adder.html")

