from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


# class HomePageView(View):
#     def get(self, request):
#         return render(request, "users/home.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing")
        else:
            context = {
                "form": login_form,
            }
            return render(request, "users/login.html", context)


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {
            "form": form
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password_1 = request.POST["password_1"]
        # password_2 = request.POST["password_2"]
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password_1
        }
        create_form = UserRegisterForm(data=data)
        if create_form.is_valid():
            create_form.save()
            return redirect("login")
        else:
            print("Error")
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class UserListView(LoginRequiredMixin, View):
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
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name_name = last_name
        user.set_password(password)
        user.save()
        return HttpResponse("<h1>Successful</h1>")
