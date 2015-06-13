# Create your views here.
from django.shortcuts import render_to_response


def custom_404(request):
    return render_to_response('404.html')


def custom_500(request):
    return render_to_response('500.html')
