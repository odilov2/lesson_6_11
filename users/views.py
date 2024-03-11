from django.contrib.auth.models import User
from django.http import HttpResponse
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


class UserListView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            users = User.objects.all()
            return render(request, "users/users_list.html", context={"users": users})
        else:
            users = User.objects.filter(first_name__icontains=search) | User.objects.filter(last_name__icontains=search)
            if not users:
                return HttpResponse("<h1>Not found</h1>")
            else:
                context = {
                    "users": users,
                    "search": search
                }
            return render(request, "users/users_list.html", context)


class UserDetailView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, "users/users_detail.html", context={"user": user})


class UserSettingsView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'users/settings.html', context={"user": user})

    def post(self, request, id):
        first_name = request.POST.get["first_name"]
        last_name = request.POST.get["last_name"]
        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name_name = last_name
        user.save()
        return HttpResponse("<h1>Success</h1>")
