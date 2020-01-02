from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.dashboard, name='app-dashboard'),
    path('upload/',views.upload, name='app-upload'),

]

#urlpatterns+=staticfiles_urlpatterns()
