from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # request는 브라우저의 요청을 의미한다.
    return HttpResponse('<h1>Hello, Inflearn!</h1>')

def index2(request):
    return render(request, "lotto/default.html", {}) # 마지막 괄호에 오브젝프틑 포함시킬 수 있음