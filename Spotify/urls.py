from django.urls import path

from . import views
urlpatterns = [
    path('', views.index,name ="dashboard"),
    path('about/',views.prediction,name = "predicty")
    
        
]
