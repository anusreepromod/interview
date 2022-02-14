from .import views
from django.urls.conf import path


urlpatterns = [
    path('logins/', views.logins, name="logins"),
    path('dashboards/', views.dashboards)
]
