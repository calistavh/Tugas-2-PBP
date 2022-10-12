from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from todolist.forms import TaskForm
from todolist.models import Task

@login_required(login_url="/todolist/login/")
def show_todolist(request):
    context = {
        "user": request.user,
        "user_id": request.user.id,
        "tasks": Task.objects.all()
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("todolist:login")
    context = {"form": form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
        else:
            messages.info(request, "Username atau Password salah!")
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("todolist:login")

@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Task telah berhasil ditambahkan!")
            return redirect("todolist:show_todolist")
    return render(request, "create_task.html")

def show_todolist_json(request):
    tasks = list(Task.objects.all().values())
    return JsonResponse(tasks, safe=False)

def add_task(request):
    form = TaskForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return JsonResponse({"title": form.instance.title, "date": form.instance.date, "description": form.instance.description})