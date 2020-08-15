from django.urls import reverse
from django.shortcuts import render
from shortner.models import Shortner
from shortner.forms import ShortnerForm
from django.views.generic.edit import View
from django.shortcuts import redirect, get_object_or_404


class ShortnerHome(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'shortner/home.html', {'title': 'Free URL Shortner', 'form': ShortnerForm()})

	def post(self, request, *args, **kwargs):
		form = ShortnerForm(request.POST)
		if form.is_valid():
			shortner = Shortner.create_short_url(short_url=form.cleaned_data.get('short_url'), original_url=form.cleaned_data.get('original_url'))
			return redirect(reverse('shortner.details', args=[shortner.short_url]))
		else:
			return render(request, 'shortner/home.html', {'title': 'Free URL Shortner', 'form':form})

class ShortnerDetails(View):
	def get(self, request, short_url, *args, **kwargs):
		shortner = get_object_or_404(Shortner, short_url=short_url, status=True)
		context = {
			'title': 'Shorterned URL : %s' % shortner.short_url, 
			'data': shortner, 
			'host': request.get_host()
		}
		return render(request, 'shortner/success.html', context)


class ShortnerRedirect(View):
	def get(self, request, short_url, *args, **kwargs):
		shortner = get_object_or_404(Shortner, short_url=short_url, status=True)
		return redirect(shortner.original_url)