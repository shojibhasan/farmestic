from django.shortcuts import redirect, render
from home.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    slide = Slider.objects.all()
    product_paginator = Product.objects.filter(is_approved = True).order_by('-date_added')[:8]
    # product_paginator = Paginator(product,12)
    context = {
        'slider': slide,
        'product_paginator':product_paginator,
    }
    return render(request, 'home/home.html',context)


def all_products(request):
    product_list = Product.objects.filter(is_approved = True)
    paginator = Paginator(product_list, 12) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    product = paginator.get_page(page_number)
    context = {
        'product': product,
    }
    return render(request, 'product/all_product.html',context)


def post_product(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.FILES['image']:
            user = request.user
            name = request.POST.get('name')
            category = request.POST.get('category')
            price = request.POST.get('price')
            description = request.POST.get('description')
            quantity = request.POST.get('quantity')
            image = request.FILES['image']
            Product.objects.create(user=user, name=name, category=category, price=price, description=description, quantity=quantity, image=image)
            messages.error(request, 'Your Product has been posted successfully')
            return render(request, 'home/post_product.html')
        return render(request, 'home/post_product.html')
    else:
        return redirect('login')
    
def product_details(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    return render(request, 'product/product_details.html',context)

def product_bid(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            get_method = request.POST.copy()
            product = get_method.get('product') or None
            quantity = get_method.get('quantity') or None
            mobile = get_method.get('mobile') or None
            bid_price = get_method.get('bid_price') or None
            message = get_method.get('message') or None
            user = request.user
            
            product_object = Product.objects.get(name=product)
            
            bid_exist = Bid.objects.filter(product=product_object,user=request.user)
            
            if not bid_exist and product_object.user != request.user:
                Bid.objects.create(product=product_object,quantity=quantity,user=user,mobile=mobile,bid_price=bid_price,message=message)
                messages.success(request, 'Bid Sent Sucessfully!')
                return redirect('/')
            else:
                messages.success(request, 'Bid Can not Done By Your Account')
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required   
def show_bids(request):
    bids = Bid.objects.all()

    context={
        'bids':bids,
    }
    return render(request, 'product/show_bids.html',context)
    
    
    
def contact(request):
    if request.method == "POST":
        get_method = request.POST.copy()
        name = get_method.get('name') or None
        email = get_method.get('email') or None
        subject = get_method.get('subject') or None
        contact_messages = get_method.get('messages') or None
        
        Contact.objects.create(name=name,email=email,subject=subject,messages=contact_messages)
        messages.success(request, 'Your Message Sent Sucessfully!')
    return render(request, 'home/contact.html')

@login_required
def profile(request):
    
    user = request.user

    user_data = User.objects.get(email=user)
    print(user_data)
    products_data = Product.objects.filter(user=user)

    
    context = {
        'user_data':user_data,
        'products_data':products_data
    }
    return render(request,'accounts/profile.html',context)

def delete(request,product_id):
    query = Product.objects.get(id=product_id)
    query.delete()
    # return HttpResponse("Deleted!")
    return redirect('profile')