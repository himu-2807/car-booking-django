from django.shortcuts import render, HttpResponse
from webapp.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from webapp.models import Booking
from django.shortcuts import redirect
from webapp.models import Car
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    context={
        "ex_variable":"This is example variable"
    }
    return render(request, "index.html", context)
    #return HttpResponse("This is home page")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact_entry=Contact(cname=cname, email=email, phone=phone, message=message)
        contact_entry.save()
    return render(request, "contact.html")

def service(request):
    cars = Car.objects.all()
    return render(request, 'service.html', {'cars': cars})   

@login_required
def booking(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        pickup_location = request.POST.get('pickup_location')
        contact_number = request.POST.get('contact_number')

        Booking.objects.create(
            user=request.user,
            car_name=car,
            pickup_date=pickup_date,
            return_date=return_date,
            pickup_location=pickup_location,
            contact_number=contact_number
        )
        messages.success(request, f"You have successfully booked {car.name}!")
        return redirect('service')  # or a "success" page
    
    return render(request, 'booking.html', {'car': car})

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "index.html")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email') 
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, "register.html")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return render(request, "register.html")
            else:
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account created successfully")
                return render(request, "login.html")

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return render(request, "index.html")