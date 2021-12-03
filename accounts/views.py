from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib import messages
# Create your views here.


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST' and request.FILES['image']:
            method_dict = request.POST.copy()
            name = method_dict.get('name')
            phone = method_dict.get('phone')
            email = method_dict.get('email')
            password = method_dict.get('password')
            address = method_dict.get('address')
            image = request.FILES['image']
            email.lower()
            
            email_exists = User.objects.filter(email=email)
            if not email_exists:
                user = User.objects.create_user(first_name=name, email=email, address=address, phone=phone, password=password, image=image)
                user.is_active = True
                user.save()
                messages.success(request, 'Registration Done Sucessfully!')
                return render(request, 'accounts/login.html')
            else:
                messages.success(request, 'Email Already Taken!')
        return render(request, 'accounts/registration.html')




def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            email.lower()
            user = authenticate(request,email=email, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        return render(request, 'accounts/login.html')
    
    
def logout(request):
    django_logout(request)
    return redirect('login')