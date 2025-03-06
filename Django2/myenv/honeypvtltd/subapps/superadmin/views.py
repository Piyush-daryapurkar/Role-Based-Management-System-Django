from django.shortcuts import render,HttpResponse,redirect
from .models import Superadmin_data,Manager_data,Manager_image
from .forms import ManagerForm,Manager_login_form

def animesh(req):
    if req.method=="POST":
        name=req.POST.get("nm")
        pasword=req.POST.get("pwd")
        data=Superadmin_data.objects.filter(username=name).exists()
        if(data):
            data1=Superadmin_data.objects.filter(password=pasword).exists()
            if(data1):
                req.session["data"]=data
                return redirect("super")
            else:
                return HttpResponse("password wrong")
            
        return HttpResponse("username wrong")
    return render(req,"superadmin.html")

def Superdashboard(req):
    data=req.session.get("data")
    btn=req.GET.get("btn")  
    print(btn)
    if data:
        if btn=='addmanager':
            if req.method=="POST":
                form=ManagerForm(req.POST)
                if form.is_valid():
                    form.save()
                    req.session['success'] = 'Manager added successfully!'
                    return redirect("super")
                else:
                    form = ManagerForm() 
                    return render(req, 'addmanager.html', {'form': form})  

            return render(req,'addmanager.html')
        elif btn=="logout":
            print(btn)
            del req.session["data"]
            return redirect("")
        elif btn=='edit':
            manager_id = req.GET.get('id')
            manager = Manager_data.objects.get(id=manager_id)
            if req.method == "POST":
                form = ManagerForm(req.POST, instance=manager)
                if form.is_valid():
                    form.save()
                    req.session['success'] = 'Manager updated successfully!'
                    return redirect("super")
            else:
                form = ManagerForm(instance=manager)
            return render(req, 'editmanager.html', {'form': form})
        elif btn=='delete':
            manager_id = req.GET.get('id')
            try:
                manager = Manager_data.objects.get(id=manager_id)
                manager.delete()
                req.session['success'] = 'Manager deleted successfully!'
            except Manager_data.DoesNotExist:
                req.session['error'] = 'Manager not found'
            return redirect("super")
            
        mdata=Manager_data.objects.all()
        return render(req,"Superdashboard.html",{"data":mdata}) 
    else:
        return redirect("")

def Manager_login(req):
    if req.method=="POST":
        email=req.POST["email"]
        password=req.POST["password"]
        memail=Manager_data.objects.filter(email=email).exists()
        if(memail):
            mpass=Manager_data.objects.filter(password=password)
            if(mpass):
                mdata=Manager_data.objects.filter(email=email)
                return render(req,"manager/Manager_profile.html",{"mdata":mdata})
            else:
                return HttpResponse("incorrect password")
        return HttpResponse("wrong email")
    form=Manager_login_form()
    return render(req,"manager/Manager_login.html",{"form":form})

def manager_update_profile(req):
    return HttpResponse("Hello")


