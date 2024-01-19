from django.contrib import admin
from .models import *


model_list = [Volonter,Događaj,Projekt]
admin.site.register(model_list)