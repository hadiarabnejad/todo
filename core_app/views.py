from django.shortcuts import render


def home(request):
    return render(request, 'core_app/coming_soon.html')
