from django.shortcuts import render
from django.shortcuts import render
from .models import Scanner
from smsApp.models import Members
from django.shortcuts import render
from scanner.models import Scanner

# Create your views here.
def ScannerView(request):
    name = Members.objects.first().first_name
    obj=Scanner.objects.get(id=1)

    context = {
        'name': name,
        'obj': obj,}
    
    return render(request, 'scanner.html', context)

   


