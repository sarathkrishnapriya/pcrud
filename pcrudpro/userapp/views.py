from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from .models import *
from . decorator import auth_user

# Create your views here.

def registraion_home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']
        pincode = request.POST['pincode']
        address = request.POST['address']
        
        sh_registraion = Registraion(name=name,password=password,email=email,
        mobile=mobile,address=address,pincode=pincode)
        sh_registraion.save()

        return render(request,'login.html',{'details':'Registration completed successfullly'})
   
    return render(request,'register.html')

def riderLoginView(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        try:
            loginViewData = Registraion.objects.get(email=username,password=password)
            request.session['ridersession'] = loginViewData.id
            return redirect('rider_home')

        except Registraion.DoesNotExist:
            return render(request,'login.html',{'details': 'Invalid credential. Try again later..'})   

    return render(request,'login.html')
 
@auth_user
def HomepageView(request):
    
    id=request.session['ridersession']

    details=Registraion.objects.get(id=id)
    return render(request,'home.html',{'details':details})

def logout(request):
    del request.session['ridersession'] 
    return redirect('rider_login')

@auth_user
def backProfileView(request):
    return redirect('rider_home')

@auth_user
def ProfileView(request):
    users_id = request.session['ridersession']
    profile_details = Registraion.objects.get(id=users_id)
    return render(request,'profile.html',{'details':profile_details})  

@auth_user
def UpdateView(request):
    users_id = request.session['ridersession']
    details = Registraion.objects.get(id=users_id)
    return render(request,'update.html',{'details':details})

def UpdateUserView(request):
    users_id = request.session['ridersession']
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']
        pincode = request.POST['pincode']
        address = request.POST['address']

        update_user = Registraion.objects.filter(id=users_id)
        update_user.update(name=name,password=password,email=email,
        mobile=mobile,address=address,pincode=pincode)
        return redirect('rider_profile')
    return render(request,'update.html')