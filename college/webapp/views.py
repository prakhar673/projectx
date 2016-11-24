from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse

from webapp.models import Colleges
# Create your views here.
def index(request):
	college_list=College.objects.get(id=2)
	return render_to_response('index.html',{'college_list': college_list})

def login_page(request):
	return render(request,'login.html')

def courses(request):
	return render(request,'courses.html')

def about(request):
	return render(request,'about.html')