from ast import If
from contextvars import Context
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
import random
from django.core.mail import send_mail
# Create your views here.

"""
===> if we want to store data in Django ORM (object relational model) or insert

# obj = Modelname.objects.create(fieldname = value,fieldname = value)
# e.g. = User.objects.create(firstname = fname,lastname = lname)

===> Retrieve data from table

There are 3 ways to retrieve data

1.) get() :- retrieve condition wise single data # get return object
# obj = Modelname.objects.get(fieldname = value)
# e.g. = User.objects.get(email = email)

====> access data e.g.
uid.email


2.) filter() :- it return query set
# retrueve data from table condition wise
# if there is posibilities to retrieve multiple data
# it will return query set

=====> access data e.g.  (queryset)
uid[index].email


3.) all() :- it will fetch all data from the model
# obj = Modelname.objects.all()
# dall = Doctor.objects.all()

"""



def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            d_count = Doctor.objects.all().count()
            context={
                'uid':uid,
                'did':did,
                'd_count':d_count
            }
            return render(request,"myapp/index.html",context)
        else:
            pid = Patient.objects.get(user_id = uid)
            p_count = Patient.objects.all().count()
            context={
                'uid':uid,
                'pid':pid,
                'p_count':p_count
            }
            return render(request,"myapp/p-index.html",context)
    else:
        return redirect('login')

def register(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.POST:
            p_firstname = request.POST['firstname']
            p_lastname = request.POST['lastname']
            p_role = request.POST['role']
            p_email = request.POST['email']
            p_contact = request.POST['contact']
            l1 = ['sdd745', 'dfsd445', 'tgrt445', 'dfr7458', '659sdsn','6568sdfn']
            #ajayrajpoot0918@gmail.com
            password = random.choice(l1)+p_email[3:6]+p_contact[4:7]

            uid = User.objects.create(email=p_email,password=password,role=p_role)
            send_mail("AUTHENTICATION", "Welcome to Medico-Expert. Your password is :" +str(password), "ajayrajpoot0918@gmail.com",[p_email],)

            if p_role == "doctor":
                did = Doctor.objects.create(user_id = uid, firstname=p_firstname, lastname=p_lastname, mobile=p_contact)
                if did:
                    print("-------> successfully register")
                    context={
                        "s_msg":"Doctor successfully registered and password has been sent on your email"
                    }
                    return render(request,"myapp/register.html",context)
                else:
                    return render(request,"myapp/register.html")

            else:
                pid = Patient.objects.create(user_id = uid, firstname=p_firstname, lastname=p_lastname, mobile=p_contact)
                if pid:
                    context={
                        "s_msg":"Patient successfully registered and password has been sent on your email"
                    }
                    return render(request,"myapp/register.html",context)
                else:
                    print("------> firstname", p_firstname)
                    return render(request,"myapp/register.html")
        else:
            print("page just loaded")
            return render(request,"myapp/register.html")
            

def login(request):
    if "email" in request.session:
        return redirect('home')
    else:
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']
            print("---> login",email)
            try:
                uid = User.objects.get(email = email)
                print("--->",uid.password)

                if uid.password == password:
                    # if uid.is_verify:
                        request.session["email"] = uid.email  # session variable

                        if uid.role == "doctor":
                            did = Doctor.objects.get(user_id = uid)

                            context={
                                "uid":uid,
                                "did":did,
                            }
                            return render(request,"myapp/index.html",context)
                        else:
                            pid = Patient.objects.get(user_id = uid)

                            context={
                                "uid":uid,
                                "pid":pid,
                            }
                            return render(request,"myapp/p-index.html")
                    # else:
                    #     pass

                else:
                    print("---> wrong password")
                    context={
                        "e_msg":"Invalid password"
                    }
                    return render(request,"myapp/login.html",context)

            except User.DoesNotExist:
                context={
                    'e_msg':"Email address does not exist"
                }
                return render(request,"myapp/login.html",context)
        else:
            return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render (request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            context={
                "uid":uid,
                "did":did,
            }
            return render(request,"myapp/profile.html",context)
    else:
        return redirect("login")


def doc_profile(request):
    try:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            did = Doctor.objects.get(user_id = uid)
            did.firstname = request.POST['firstname']
            did.lastname = request.POST['lastname']
            did.qualification = request.POST['qualification']
            did.specification = request.POST['specification']
            did.available_time = request.POST['available_time']
            did.experiance = request.POST['experiance']
            did.clinic_name = request.POST['clinic_name']
            did.clinic_city = request.POST['clinic_city']
            did.clinic_address = request.POST['clinic_address']
            did.mobile = request.POST['mobile']
            if "pic" in request.FILES:
                did.pic = request.FILES['pic']
            did.save()
            context = {
                    "uid":uid,
                    "did":did,
                    "s_msg":"Successfully Profile Update"
            }
            return render(request,"myapp/profile.html", context)
        else:
            return redirect("login")
    except:
        return redirect("login")

def patients_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "patient":
            pid = Patient.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'pid' : pid,
            }
            return render(request, "myapp/patients-profile.html", context)


def pt_profile(request):
    try:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            pid = Patient.objects.get(user_id = uid)
            pid.firstname = request.POST['firstname']
            pid.lastname = request.POST['lastname']
            pid.address = request.POST['address']
            pid.mobile = request.POST['mobile']
            if "pic" in request.FILES:
                pid.pic = request.FILES['pic']
            pid.save()
            context = {
                    "uid":uid,
                    "pid":pid,
                    "s_msg":"Successfully Profile Update"
            }
            return render(request,"myapp/patinets-profile.html", context)
        else:
            return redirect("login")
    except:
        return redirect("login")


def doc_pass_change(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']
            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                del request.session['email']
                context={
                    "uid":uid,
                    "did":did,
                    "s_msg":"Password changed successfully"
                }
                return render(request,"myapp/login.html", context)
            else:
                e_msg = "Invalid current password"
                context={
                    "uid":uid,
                    "did":did,
                    "e_msg":e_msg
                }
                return render(request,"myapp/profile.html", context)

def all_doctors(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            dall = Doctor.objects.filter().exclude(user_id=uid)
            context={
                'did': did,
                'dall':dall,
                'uid':uid,
            }
            return render(request,"myapp/all-doctors.html", context)

def p_all_doctors(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        pid = Patient.objects.get(user_id = uid)
        dall = Doctor.objects.all()
        context={
            'uid':uid,
            'pid':pid,
            'dall':dall,
        }
        return render(request,"myapp/p-all-doctors.html", context)

def view_doc(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            did_s = Doctor.objects.get(id=pk)
            context={
                'did':did,
                'uid':uid,
                'did_s':did_s,
            }
            return render(request,"myapp/doc-spe-profile.html", context)

def change_password(request):
    try:
        if request.POST:
            email = request.POST['email']
            oldpassword = request.POST['oldpassword']
            newpassword = request.POST['newpassword']
            confirmpassword = request.POST['confirmpassword']

            uid = User.objects.get(email = email)
            if uid.password == oldpassword and newpassword == confirmpassword:
                context = {
                    's_msg':"Successfully password reset"
                }
                return render(request,"myapp/login.html",context)
            else:
                ontext = {
                    'e_msg':"Invalid password or does not match password"
                }
                return render(request,"myapp/login.html",context)

        else:
            return render(request,"myapp/login.html")

    except:
        return render(request,"myapp/login.html")


def p_doc_spe_profile(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        pid = Patient.objects.get(user_id = uid)
        did_s = Doctor.objects.get(id = pk)
        context={
            'uid':uid,
            'pid':pid,
            'did_s':did_s,
        }
        return render(request,"myapp/p-doc-spe-profile.html", context)
