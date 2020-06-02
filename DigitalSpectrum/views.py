from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegisterForm
import csv
import os


from .models import Sensor, Category, Cart, Checkout, Unit, System, Crop
from django.contrib.auth.models import User

# Homepage

def index(request):
    return render(request, "index.html")


def crops(request):
    return render(request, "crops.html")

def dash(request):
    sensors = Sensor.objects.all()
    units = Unit.objects.all()
    systems = System.objects.all()
    crops = Crop.objects.all()

    context = {
        "sensors": sensors,
        "units": units,
        "systems": systems,
        "crops": crops,


    }
    return render(request, "dash.html", context)

def account(request):
    sensors = Sensor.objects.all()
    units = Unit.objects.all()

    context = {
        "sensors": sensors,
        "units": units,

    }

    return render(request, "account.html", context)

def support(request):
    return render(request, "support.html")

def user_setup(request):
    return render(request, "user_setup.html")


# Register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {'form' : form})


# Shop
def shop(request):

    context = {
            "baro": Sensor.objects.get(pk=6),
            "ph": Sensor.objects.get(pk=5),
            "moist": Sensor.objects.get(pk=4),
            "water": Sensor.objects.get(pk=3),
            "air": Sensor.objects.get(pk=2),
            "tds": Sensor.objects.get(pk=1),
            "start": Sensor.objects.get(pk=7),
            "adv": Sensor.objects.get(pk=8),
            "cart": Cart.objects.all()[0]
    }
    return render(request, "shop.html", context)

# Add Item to Cart
def add_cart(request, sensor_id):

    cart = Cart.objects.all()[0]

    try:
        sensor_id = int(request.POST["sensorItem"])
        # size_id = int(request.POST["itemSize"])
        print(sensor_id)
        # size = Size.objects.get(pk=size_id)
        sensor = Sensor.objects.get(pk=sensor_id)
        # recipe = get_object_or_404(Recipe, pk=menu_id)


    except KeyError:
        return render(request, "error.html", {"message": "No selection"})
    except Senesor.DoesNotExist:
        return render(request, "error.html", {"message": "No Sensor"})
    except Cart.DoesNotExist:
        return render(request, "error.html", {"message": "No Cart"})

    cart.cart_item.add(sensor)
    # cart.size.add(size)

    return HttpResponseRedirect(reverse("shop"))

# Purchase Page when complete
def purchase(request):
    return render(request, "purchase.html")

# Create your views here.
def about(request):
    return render(request, "about.html")

# Create your views here.
def purchase(request):
    return render(request, "purchase.html")

# Single Item Page
def sensor_item(request, sensor_id):
    sensors = Sensor.objects.all()
    units = Unit.objects.all()

    try:
        sensor = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
        raise Http404("Item does not exist.")

    context = {
        "sensor": sensor,
        "sensors": sensors,
        "units": units


    }
    return render(request, "sensor.html", context)




# Cart Checkout Page
def cart(request):
    checkout = Checkout.objects.get(pk=1)
    new_total = 0

    for item in checkout.cart.all():
        for cart_item in item.cart_item.all():
            new_total += cart_item.price
        print(new_total)


    context = {
        "Cart": Cart.objects.all(),
        "checkout": checkout,
        "new_total": new_total

    }
    return render(request, "cart.html", context)

# Create your views here.
def active_sensors(request):
        sensors = Sensor.objects.all()
        context = {
            "sensors": sensors,
            "baro": Sensor.objects.get(pk=6),
            "ph": Sensor.objects.get(pk=5),
            "moist": Sensor.objects.get(pk=4),
            "water": Sensor.objects.get(pk=3),
            "air": Sensor.objects.get(pk=2),
            "tds": Sensor.objects.get(pk=1),
            "cart": Cart.objects.all()[0]
        }
        return render(request, "active_sensors.html", context)

# Purchase Page when complete
def purchase(request):
    return render(request, "purchase.html")


# Purchase Page when complete
def contact(request):
    return render(request, "contact.html")
