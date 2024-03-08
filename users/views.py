from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render, redirect


class HomePageView(View):
    def get(self, request):
        return render(request, 'users/home.html')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if len(user) == 0:
            return redirect('login')
        else:
            return redirect('home')


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('login')

