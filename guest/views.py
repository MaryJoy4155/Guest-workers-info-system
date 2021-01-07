from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from guest.models import GuestWorker, Sponsor, Contractor


class IndexView(TemplateView):
    template_name = 'index.html'
class AdminView(TemplateView):
    template_name = 'login.html'
class UserView(TemplateView):
    template_name = 'user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username=self.request.user)
        return context

class RegisterView(TemplateView):
    template_name = 'register.html'

    def post(self,request,*args,**kwargs):
        email= request.POST['email']
        fname= request.POST['fname']
        lname= request.POST['lname']
        gender= request.POST['gender']
        dob=request.POST['DOB']
        paddress= request.POST['paddress']
        taddress= request.POST['taddress']
        phone=request.POST['contact']
        district= request.POST['district']
        state= request.POST['state']
        qualification= request.POST['qualification']
        adharnumber=request.POST['adhar']
        idprooof= request.FILES['proof']
        photo= request.FILES['photo']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']

        try:

            u = User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname)
            u.save()

            w = GuestWorker()
            w.user = u
            w.gender = gender
            w.dob = dob
            w.contact = phone
            w.AdharNumber = adharnumber
            w.District = district
            w.PermanantAddress = paddress
            w.TemporaryAddress = taddress
            w.Qualification = qualification
            w.State = state
            w.IDproof = idprooof
            w.Photo = photo

            w.save()
            return render(request,'index.html',{'message':"Registered"})
        except:

            return render(request,'index.html',{'message':"User Already Exist"})



class RegisterView_contractor(TemplateView):
    template_name = 'reg_contractor.html'

    def post(self,request,*args,**kwargs):
        email= request.POST['email']
        fname= request.POST['fname']
        lname= request.POST['lname']
        gender= request.POST['gender']
        dob=request.POST['DOB']
        paddress= request.POST['paddress']
        taddress= request.POST['taddress']
        phone=request.POST['contact']
        district= request.POST['district']
        state= request.POST['state']
        adharnumber=request.POST['adhar']
        idprooof= request.FILES['proof']
        photo= request.FILES['photo']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']

        try:

            u = User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname)
            u.save()

            c = Contractor()
            c.user = u
            c.gender = gender
            c.dob = dob
            c.contact = phone
            c.AdharNumber = adharnumber
            c.District = district
            c.PermanantAddress = paddress
            c.TemporaryAddress = taddress
            c.State = state
            c.IDproof = idprooof
            c.Photo = photo

            c.save()
            return render(request,'index.html',{'message':"Registered"})
        except:

            return render(request,'index.html',{'message':"User Already Exist"})



class RegisterView_sponsor(TemplateView):
    template_name = 'reg_sponsor.html'

    def post(self,request,*args,**kwargs):
        email= request.POST['email']
        fname= request.POST['fname']
        lname= request.POST['lname']
        gender= request.POST['gender']
        dob=request.POST['DOB']
        paddress= request.POST['paddress']
        taddress= request.POST['taddress']
        phone=request.POST['contact']
        district= request.POST['district']
        state= request.POST['state']
        adharnumber=request.POST['adhar']
        idprooof= request.FILES['proof']
        photo= request.FILES['photo']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']

        try:

            u = User.objects.create_user(username=email,password=password,first_name=fname,last_name=lname)
            u.save()

            s = Sponsor()
            s.user = u
            s.gender = gender
            s.dob = dob
            s.contact = phone
            s.AdharNumber = adharnumber
            s.District = district
            s.PermanantAddress = paddress
            s.TemporaryAddress = taddress
            s.State = state
            s.IDproof = idprooof
            s.Photo = photo

            s.save()
            return render(request,'index.html',{'message':"Registered"})
        except:

            return render(request,'index.html',{'message':"User Already Exist"})





class LoginView(TemplateView):
    template_name = 'login.html'
    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                else:
                    return  redirect('/worker')
            else:
                return render(request,'index.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'index.html',{'message':"Invalid Username or Password"})

class SignUp(TemplateView):
    template_name = 'SignUp.html'

class Reg_contractor(TemplateView):
    template_name = 'reg_contractor.html'

class Reg_sponsor(TemplateView):
    template_name = 'reg_sponsor.html'