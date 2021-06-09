from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Profile
from .models import Category
from .models import Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def index(request):
    products = None
    category_id = request.GET.get("category")
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    params = {}
    params["products"] = products
    params["categories"] = categories
    return render(request, "index.html", params)


def signup(request):
    if request.method == "POST":
        # get the post parameters
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordcon = request.POST.get("passwordcon")
        bio = request.POST.get("bio")
        location = request.POST.get("location")

        # check for errorneos input
        # username for upto 10 characters
        if len(username) > 10:
            messages.warning(request, "Username must be under 10 characters")
            return redirect("index")

        # username upto 10 characters
        if not username.isalnum():
            messages.warning(
                request, "Username should only contain letters and numbers"
            )
            return redirect("index")

        # for matching password
        if password != passwordcon:
            messages.warning(request, "Password doesn't match enter carefully")
            return redirect("index")

        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        data=Profile(user=myuser,bio=bio,location=location)
        data.save()
        messages.success(request, "Your E-Shop account is successfully created")
        return redirect("index")
    else:
        return HttpResponse("error 404")


def Handlelogin(request):
    if request.method == "POST":
        # get the post parameters
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect("index")
        else:
            messages.warning(request, "Invalid Credentials,Please try again")
            return redirect("index")
    else:
        return HttpResponse("error 404")


def Handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("index")


def cart(request):
    context = {}
    items = Cart.objects.filter(user__id=request.user.id)
    context["items"] = items
    if request.user.is_authenticated:
        if request.method == "POST":
            prod_id = request.POST["prod_id"]
            product = Product.objects.get(id=prod_id)
            qty = request.POST["qty"]
            is_exist = Cart.objects.filter(
                product__id=prod_id, user__id=request.user.id
            )
            if len(is_exist) > 0:
                messages.success(request, "Item already exists in your cart")
            else:
                cart = Cart(
                    user=request.user,
                    product=product,
                    quantity=qty,
                    added_on=timezone.now(),
                    update_on=timezone.now(),
                )
                cart.save()
                messages.success(request, "Item added in your cart")

    else:
        context["status"] = "Please login to view your Cart"
    return render(request, "cart.html", context)

def updateprofile(request):
    context={}
    data = Profile.objects.get(user__id=request.user.id)
    context={'data':data}
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        bio=request.POST['bio']
        location=request.POST['location']
        user=User.objects.get(id=request.user.id)
        user.first_name=firstname
        user.last_name=lastname
        user.email=email
        user.save()
        data.bio=bio
        data.location=location
        data.save()
    return render(request,'updateprofile.html',context)
    
