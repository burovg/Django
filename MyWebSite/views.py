from django.http import HttpResponse
from django.shortcuts import *
from django.views import View


import models
import forms



def Person(request, month, year):

    str = models.GetPersonGreet(month, year)
    return HttpResponse(str)

def test():
    return "OK"

def Hello(request):
    return HttpResponse(test())

def Contact(request):
    return HttpResponse("Contact Page")

def HomePage(request):
    return render(request, 'HomePage.html' , { 'Name' : request.session['Test'] })


def GreetPage(request):
    return render(request, 'GreetPage.html' , { 'City' : 'TLV' })




def StudentData(request):
    arr = [80,90,95 ]
    return render(request, 'StudentPage.html', {'Name' : 'Avi Ron', 'Faculty' : 'CS', 'Grades' : arr, 'index' : range(len(arr)), 'Avg' : models.CalcAvg(arr)})


def Products(request):
    return render(request, 'ProductsPage.html', {'Products' : models.GetProducts() })


def Product(request,id):
    prod = models.GetProduct(id)[0]
    return render(request, 'ProductPage.html', {'Product' : prod })


class MyClassView(View):
        def get(self,request):
            myFrm = forms.MyForm()
            return render(request,'EmptyForm.html', {'frm' : myFrm } )

        def post(self, request):
            dataFrm = forms.MyForm(request.POST)
            if dataFrm.is_valid():
                return HttpResponse(dataFrm.cleaned_data['name'])

