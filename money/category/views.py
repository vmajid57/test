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

			# TODO: think about why template just give dict
			result = Category.objects.values('source').annotate(total_price=Sum('price'))

			return HttpResponse(template.render({'form': form, 'cat': Category.objects.all()}, request))
	else:
		form = InputExpense()

		result = Category.objects.values('source').annotate(total_price=Sum('price'))

	# TODO: why this line was out of the block? i don't know why
	return render(request, 'expense.html', {'form': form, 'cat': Category.objects.all()})  # pass that form to the template


def thanks(request):
	return HttpResponse("think you")
