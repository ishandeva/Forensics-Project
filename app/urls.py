from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
#from .views import ParseExcel

urlpatterns = [

    path('', views.dashboard, name='app-dashboard'),
    path('upload/',views.upload, name='app-upload'),
    path('datawizard/', include('data_wizard.urls')),

]

#urlpatterns+=staticfiles_urlpatterns()
