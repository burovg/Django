
from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^HomePage/', views.Hello),
    url(r'^HomePageTemplate/', views.HomePage),
    url(r'^HomePages/', views.Hello),
    url(r'^Greet/', views.GreetPage),
]
