from .import views
from django.urls.conf import path

urlpatterns = [

    path('registration/', views.registration, name='registration'),
    path('fnlogin/', views.fnlogin, name='fnlogin'),
    path('dashboard/', views.dashboard)


]
