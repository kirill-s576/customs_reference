from django.contrib import admin
from django.urls import path, include
from . import views, ajax

urlpatterns = [
    # AJAX
    path('check_country_form/', ajax.check_country_form),
    path('create_country_form/', ajax.create_new_country),

    path('check_payment_form/', ajax.check_payment_form),
    path('create_payment_form/', ajax.create_new_payment),

    # Sheets
    path('payments_reference', views.payments_reference),
    path('country_reference', views.country_reference),
    path('add_payment', views.add_payment),
    path('add_country', views.add_country),
    path('excel_adder', views.excel_adder),
    path('', views.main)
]