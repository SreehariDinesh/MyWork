from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import logout as logouts
from.models import Register,Gallery
from .forms import Registerform,Loginform,Updateform,ChangepasswordForm

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render (request,'index.html')

def registration(request):
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['Confirmpassword']

            user=Register.objects.filter(Email=email).exists()  
            if user:
                messages.warning(request,'email already exist')
                return redirect('/login')
            elif password!=confirmpassword:
                messages.success(request,'password missmatch')
            else:
                tab=Register(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                
                
                subject = 'welcome to ewrewrtetgre'
                message = f'Hi {name}, thank you for registering in rgrthytyhrt.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )

                
                messages.success(request,'DATA SAVED')
                return redirect('/login')
    else:
        form=Registerform()
    return render(request,'registration.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=Loginform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Register.objects.get(Email=email)
                if not user:
                   messages.warning(request,'Email does not exist')
                   return redirect('/login')
                elif password!=user.Password:
                   messages.warning(request,'password incorrect')
                   return redirect,('/login')
                else:
                   messages.success(request,'Success')
                   return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'email or password incorrect')
                return redirect('/login')
    else:
        form=Loginform()
    return render(request,'login.html',{'form':form})   

def home(request,id):
    user=Register.objects.get(id=id)
    return render(request,'home.html',{'user':user})    

def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=Updateform(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/home/%s' % user.id)
    else:
        form=Updateform(instance=user)
    return render(request,'update.html',{'user':user,'form':form}) 

def delete(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    messages.success(request,'Success')
    return redirect('/')

def logout(request):
    logouts(request)
    messages.success(request,("logged out"))
    return redirect('/')

def changepassword(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=ChangepasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['Oldpassword']
            newpassword=form.cleaned_data['Newpassword']
            confirmpassword=form.cleaned_data['confirmpassword']
            
            if oldpassword!=user.Password:
                messages.warning(request,'incorrect')
                return redirect('/changepassword/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'password similar')
                return redirect('/changepassword/%s' % user.id)
            elif newpassword==confirmpassword:
                messages.warning(request,'new password')
                return redirect('/changepassword/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,'change success')
    else:
        form=ChangepasswordForm()
        return render(request,'changepassword.html',{'user':user, 'form':form})            

def gallery(request):
    images=Gallery.objects.all()
    return render(request,'gallery.html',{'images':images})

def details(request,id):
    images=Gallery.objects.get(id=id)
    return render(request,'details.html',{'images':images})
    

               
                
                    
