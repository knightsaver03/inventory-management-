from django.shortcuts import render

# Create your views here.

def startup_view(request):
	return render(request, 'inventory_managment/base.html')