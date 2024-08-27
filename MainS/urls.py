from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name ="Usersearching"),    
]
