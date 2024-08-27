
from django.shortcuts import render
from .models import Songs
# Create your views here.

def home(request):
    song = Songs.objects.all()
    if request.method == 'POST':
        searched = request.POST.get('query')
        if searched is not None:
            song = song.filter(Track_Name = searched)
            context = {
                'qs': song
            }
            print("This is POST of user search")
            return render(request,'home.html',context)
            
    else:
        print("This is GET")
        return render(request,'home.html')
