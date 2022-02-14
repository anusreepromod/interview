from django.shortcuts import render
from .models import *

# Create your views here.


def registration(request):
    try:
        email = request.POST['email']
        print(email)
        u_obj = login.objects.filter(username=email).exists()
        if u_obj == False:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            password = request.POST['pass']
            reg_obj = register(name=name, email=email,
                               mobile=mobile)
            reg_obj.save()
            log_obj = login(username=email, password=password,
                            user_id_id=reg_obj.id)
            log_obj.save()
            return render(request, 'login.html')
    except Exception as e:
        print(e)
    return render(request, 'registration.html')


def fnlogin(request):
    try:
        username = request.POST['email']
        print(username)
        password = request.POST['pass']
        print(password)
        logi_obj = login.objects.get(username=username, password=password)
        print(logi_obj)
        request.session['log'] = logi_obj.id
        log_obj = register.objects.get(id=logi_obj.user_id_id)
        user = log_obj.name
        return render(request, 'dashboard.html', {'user': user})
    except Exception as e:
        print(e)
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
