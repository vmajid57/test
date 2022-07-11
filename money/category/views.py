from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputExpence
from .models import Category
from django.db.models import Sum

def add_expence(request):
	if request.method == 'POST':
		form = InputExpence(request.POST)  # instantiate a new form here

		if form.is_valid():
			template = loader.get_template('expense.html')
			form.save()
			
			sumOfPrice = Category.objects.aggregate(Sum('price')) #sum of all prices
			
			# for create object from source and price
			arr = []
			context = {}
			
			for item in Category.objects.all():
				# every row > {'source' : price}
				temp = {}
				temp[item.source] = item.price
				arr.append(temp) #every row append to array
			
			#final dic for pass to template. i don't know why i do this :))
			#cat is name for key
			context['cat'] = arr 
			return HttpResponse(template.render(context, request))        
	else:
		form = InputExpence()
	
	return render(request,'expense.html',{'form': form})  # pass that form to the template

def thanks(request):
	return HttpResponse("thnk you")