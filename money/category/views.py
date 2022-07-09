from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputExpence

def add_expence(request):
	if request.method == 'POST':
		form = InputExpence(request.POST)  # instantiate a new form here

		if form.is_valid():
			# source = form.cleaned_data['source'],
			# price = form.cleaned_data['price']
			form.save()
			return HttpResponseRedirect('/expense/')
	else:
		form = InputExpence()
	
	return render(request,'expense.html',{'form': form})  # pass that form to the template

def thanks(request):
	return HttpResponse("thnk you")