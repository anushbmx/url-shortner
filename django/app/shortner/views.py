from django.shortcuts import render

def home(request):
    return render(request, 'shortner/home.html', {})


def success(request):
    return render(request, 'shortner/success.html', {})
