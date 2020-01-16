from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from .views import ParseExcel

urlpatterns = [

    path('', views.dashboard, name='app-dashboard'),
    path('upload/',views.upload, name='app-upload'),
    #path('upload/',ParseExcel.as_view(), name='app-upload'),

]

#urlpatterns+=staticfiles_urlpatterns()
