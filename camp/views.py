from django.shortcuts import render
from django.http import HttpResponse
from basicauth.decorators import basic_auth_required

@basic_auth_required
def index(request):
   return render(request, 'camp/index.html')

def search(request):
   return render(request, 'camp/search.html')

def detail(request):
   return render(request, 'camp/detail.html')

def reservation_apply(request):
   return render(request, 'camp/reservation_apply.html')

def reservation_complite(request):
   return render(request, 'camp/reservation_complite.html')