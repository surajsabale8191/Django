from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    context ={
        "variable":"This is sent"
    }
    return render(request, "index.html", context)
    #return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse(" THis is services page")

def contact(request):
    return HttpResponse(" THis is contact page")