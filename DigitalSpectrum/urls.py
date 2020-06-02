from django.urls import path, include
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),

    path("login", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path("register", views.register, name="register"),


    path("<int:sensor_id>", views.sensor_item, name="sensor"),


    path("shop", views.shop, name="shop"),
    path("shop/<int:sensor_id>", views.add_cart, name="add_cart"),
    path("cart", views.cart, name="cart"),

    path("dash", views.dash, name="dash"),
    path("crops", views.crops, name="crops"),

    path("account", views.account, name="account"),
    path("support", views.support, name="support"),
    path("user_setup", views.user_setup, name="user_setup"),

    path("contact", views.contact, name="contact"),
    path("purchase", views.purchase, name="purchase"),
    path("active_sensors", views.active_sensors, name="active_sensors"),

]
