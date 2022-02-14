from django.shortcuts import render
from formapp.models import *
from . models import *
# Create your views here.


def logins(request):
    if request.method == 'POST':
        username = request.POST['email']
        print(username)
        password = request.POST['pass']
        print(password)
        logi_obj = adminlogin.objects.get(
            username=username, password=password)
        print(logi_obj)
        request.session['log'] = logi_obj.id
        user = register.objects.all()
        return render(request, 'dashboards.html', {'user': user})
    return render(request, 'adminlogin.html')


def dashboards(request):
    user = register.objects.all()
    return render(request, 'dashboards.html', {'user': user})
