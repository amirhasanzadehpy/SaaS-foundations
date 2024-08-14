from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username') or None
        password = request.POST.get('password') or None
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    return render(request, "auth/login.html", {})



def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username') or None
        password = request.POST.get('password') or None
        email = request.POST.get('email') or None
        if all([username, password, email]):
            try:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('/login')
            except:
                pass
    return render(request,"auth/register.html", {})