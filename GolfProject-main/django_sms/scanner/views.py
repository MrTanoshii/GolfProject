from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Scanner



from django.views.generic import ListView
from .models import Scanner

class ScannerView(ListView):
    model = Scanner
    template_name = 'scanner.html'

