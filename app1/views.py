from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404
from .form import *
from .models import *

# Create your views here.




@login_required(login_url="login")
def index(request):
    ctx = {
        "posts": Posts.objects.all().order_by("-id"),
        "comment": Comment.objects.all().order_by("-id"),
        }
    # Creating Comment
    if request.method == "POST":
        comment = CreateComment(request.POST)
        post_id = request.POST.get('post_id')
        if comment.is_valid():
            post = get_object_or_404(Posts, pk=post_id)

            final = comment.save(commit=False)
            final.user = request.user
            final.post = post
            final.save()
            return render(request, "index.html", ctx)

    return render(request, "index.html", ctx)



@login_required(login_url="login")
def post(request):
    ctx = {}
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect("/home")
    return render(request, "add-post.html", ctx)



@login_required(login_url="login")
def filter_author(request):
    user_id = int(request.GET.get("user", request.user.id))
    ctx = {
        "users": User.objects.all().order_by("-pk"),
    }
    posts = Posts.objects.filter(author_id=user_id).order_by("-id")
    ctx["posts"] = posts
    ctx["user_id"] = user_id
    return render(request, "filter-author.html", ctx)




def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            result = check_password(password, user.password)
            if result:
                 login(request, user)
                 return redirect("/home")
            else:
                 ctx = {"error": "Something gone wrong!!!"}
        else:
            ctx = {"error": "Something gone wrong!!"}
    else:
        ctx = {}
    return render(request, "registration/login.html", ctx)




def register(request):
    message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
        else:
            message = "Something went wrong!!!"
    else:
        form = RegistrationForm()

    ctx = {
        "form": form,
        "message": message
    }
    return render(request, "register.html", ctx)


