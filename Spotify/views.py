from django.shortcuts import render
from MainS.models import Songs
import joblib
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    
        song = Songs.objects.all()
        if request.method == 'POST':
            searched = request.POST.get('query')
            if searched is not None:
                song = song.filter(Track_Name__icontains = searched)
                context = {
                    'qs': song
                }
                print("This is POST of Spotify search")
                return render(request,'a.html',context)
                
        else:
            print("This is GET")
            return render(request,'index.html')

def prediction(request):
    
    print("Comes to prediction")
    
    model = joblib.load('Model1.sav')

    lis = []
    if request.method == 'POST':
        print("This is post")
        lis.append(request.POST.get('acousticness'))
        lis.append(request.POST.get('danceability'))
        lis.append(request.POST.get('duration_ms'))
        lis.append(request.POST.get('energy'))
        lis.append(request.POST.get('explicit'))
        lis.append(request.POST.get('instrumentalness'))
        lis.append(request.POST.get('key'))
        lis.append(request.POST.get('liveness'))
        lis.append(request.POST.get('loudness'))
        lis.append(request.POST.get('mode'))
        lis.append(request.POST.get('speechiness'))
        lis.append(request.POST.get('tempo'))
        lis.append(request.POST.get('valence'))
        
        print(lis)
        ans = model.predict([lis])
        print("goes to POST")
        return render(request,"index.html",{'ans':ans,'lis':lis}) 

    else:
        print("goes to GET")
        return render(request,"index.html")



    