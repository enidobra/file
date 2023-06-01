from django.urls import path
from.import views

urlpatterns=[
    path("", views.home, name="home"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("activities/", views.activities, name="activities"),
    path("contact/", views.contact, name="contact"),
    path("fullblog/<id>", views.fullblog, name="fullblog"),
    path("packages/", views.packages, name="packages")
]
