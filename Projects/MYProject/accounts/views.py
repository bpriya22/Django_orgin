from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # print("username taken")
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print("email already in use")
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                #when we want the form data to be stored on database. 4 lines necessary
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                #print('user created')
                messages.info(request,"User Created")
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/') #to redirect to home page

    else:
        return render(request,'register.html')