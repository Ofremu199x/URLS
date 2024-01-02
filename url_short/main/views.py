from django.shortcuts import render
import pyshorteners
import pyperclip
from django.contrib import messages

# Create your views here.


def home(request):
    
    
    
    
    return render (request, 'home.html')


def result(request):
    
    url = request.POST['url']
    url_shortener = pyshorteners.Shortener()
    short_url = url_shortener.tinyurl.short(url)
    st = str(short_url)
    #cp = pyperclip.copy(st)
    #messages.success(request,'The url has been copied to the clipboard') 
    
    return render (request, 'result.html',{'st':st })