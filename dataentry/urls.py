from django.contrib import admin
from django.urls import path,include

from dataentry import views

urlpatterns = [
    path('import-data/',views.import_data,name='import_data'),
    path('export-data/',views.export_data,name='export_data'),
]