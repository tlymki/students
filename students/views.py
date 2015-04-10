from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return render(request, 'students/students_list.html', {})
    # return HttpResponse("<h1> Hello world </h1>" )
# Create your views here.
