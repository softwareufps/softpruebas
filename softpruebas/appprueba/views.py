from django.shortcuts import render

# Create your views here.

def vistasqli(request):
	pagina="vistasqli.html"
	return render(request, pagina)
