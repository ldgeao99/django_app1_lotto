from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import GuessNumbers


def index(request): # request는 브라우저의 요청을 의미한다.
    return HttpResponse('<h1>Hello, Inflearn!</h1>')

def index2(request):
    lottos = GuessNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos" : lottos}) # 마지막 괄호에 있는건 딕셔너리 형태로 {}상태로 그냥 놔둬도 무관.
