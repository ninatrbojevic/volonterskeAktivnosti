from django.shortcuts import render
from django.http import HttpResponse

## Create your views here.
def homepage(request):
    return HttpResponse('Dobrodošli na stranicu za <strong>volontiranje</strong>!')
    # primjetiti korištenje HTML-a