
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.send_to_home),
    path('home', views.home),
    path('contact-us', views.contact_us),
    path('our-company', views.our_company)
]

