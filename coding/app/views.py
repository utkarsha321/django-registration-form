from django.shortcuts import render,HttpResponse
from .models import Reg
# Create your views here.
def index(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphone=request.POST.get("num")
        fage=request.POST.get("age")
        fstate=request.POST.get("state")
        fcountry=request.POST.get("country")
        #print(name,email,phone,age,state,country)
        register=Reg(name=fname,email=femail,phone=fphone,age=fage,state=fstate,country=fcountry)
        register.save()
        return HttpResponse("Your Record has been saved")
    return render(request,'index.html')


