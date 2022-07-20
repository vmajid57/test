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
			for item in Category.objects.all():
				# every row > {'source' : price}
				temp = {}
				temp[item.source] = item.price
				arr.append(temp) #every row append to array
			
			#TODO: think about why template just give dict
			#cat is name for key
			return HttpResponse(template.render({'form': form, 'cat': arr}, request))        
	else:
		form = InputExpence()
		#TODO: do this for loop once. this loop repeat in if and else block.
		arr = []
		for item in Category.objects.all():
			# every row > {'source' : price}
			temp = {}
			temp[item.source] = item.price
			arr.append(temp)
	#TODO: why this line was out of the block? i dont know why
	return render(request,'expense.html',{'form': form, 'cat': arr})  # pass that form to the template

def thanks(request):
	return HttpResponse("thnk you")