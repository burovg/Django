
from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^HomePage/', views.Hello),
    url(r'^HomePageTemplate/', views.HomePage),
    url(r'^ContactUs/', views.Contact),
      url(r'^Greet/', views.GreetPage),
    url(r'^student/', views.StudentData),
    url(r'^person/(\d{2})/(\d{4})', views.Person),
    url(r'^products/', views.Products),
   url(r'^product/(\d{1})', views.Product),
    url(r'^emptyform/', views.MyClassView.as_view())

]
