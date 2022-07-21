from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputExpense
from .models import Category
from django.db.models import Sum


def add_expense(request):
	if request.method == 'POST':
		form = InputExpense(request.POST)  # instantiate a new form here

		if form.is_valid():
			template = loader.get_template('expense.html')
			form.save()
			
			sumofprice = Category.objects.aggregate(Sum('price'))  # sum of all prices
			# for create object from source and price
			arr = []
			for item in Category.objects.all():
				# every row > {'source' : price}
				temp = {item.source: item.price}
				arr.append(temp)  # every row append to array
			
			# TODO: think about why template just give dict
			# cat is name for key
			result = Category.objects.values('source').annotate(total_price=Sum('price'))

			print(result)
			return HttpResponse(template.render({'form': form, 'cat': arr}, request))        
	else:
		form = InputExpense()
		# TODO: do this for loop once. this loop repeat in if and else block.
		arr = []
		for item in Category.objects.all():
			# every row > {'source' : price}
			temp = {item.source: item.price}
			arr.append(temp)
		result = Category.objects.values('source').annotate(total_price=Sum('price'))
		print(result)

	# TODO: why this line was out of the block? i don't know why
	return render(request, 'expense.html', {'form': form, 'cat': arr})  # pass that form to the template


def thanks(request):
	return HttpResponse("think you")
