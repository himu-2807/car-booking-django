from django.contrib import admin
from django.urls import path
from webapp import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name="index"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("service/",views.service, name="service"),
    path("login/",views.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path("register/",views.register, name="register"),
    path('booking/<int:car_id>/', views.booking, name='booking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
