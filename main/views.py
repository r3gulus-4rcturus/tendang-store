import datetime
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.forms import ProductForm
from django.utils.html import strip_tags
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "")
            return redirect('main:show_main')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect("main:show_main")
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('username', user.username)
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('username')
    return response

@csrf_exempt
def register_ajax(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({"success": True, "message": "Account created successfully!"})
        else:
            # Return form errors in JSON
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=400)


@csrf_exempt
def login_ajax(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({
                "success": True,
                "message": "Login successful!",
                "redirect_url": reverse("main:show_main")
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('username', user.username)
            return response
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=400)


@csrf_exempt
def logout_ajax(request):
    if request.method == "POST":
        logout(request)
        response = JsonResponse({"success": True, "message": "Logged out successfully."})
        response.delete_cookie('last_login')
        response.delete_cookie('username')
        return response
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=400)

@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        'name': request.user.username,
        'kelas': 'PBP A',
        'npm':'2406362860',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

# @login_required(login_url='/login')
# def create_product(request):
#     form = ProductForm(request.POST or None)
    
#     if form.is_valid() and request.method == "POST":
#         product_entry = form.save(commit=False)
#         product_entry.user = request.user
#         product_entry.user
#         form.save()
#         return redirect('main:show_main')
    
#     context = {"form": form}
#     return render(request, "create_product.html", context)

# @login_required(login_url='/login')
# def edit_product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     form = ProductForm(request.POST or None, instance=product)
#     if form.is_valid() and request.method == 'POST':
#         form.save()
#         return redirect('main:show_main')

#     context = {
#         'form': form
#     }

#     return render(request, "edit_product.html", context)

@login_required(login_url='/login')
@csrf_exempt
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
    
def show_product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "show_product.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

# def show_json(request):
#     product_list = Product.objects.all()
#     json_data = serializers.serialize("json", product_list)
#     return HttpResponse(json_data, content_type="application/json")

def show_json(request):
    product_list = Product.objects.all()
    json_data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'description': product.description, 
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'seller_id': product.user.id if product.user else None,
            'seller_name': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    
    return JsonResponse(json_data, safe=False) # safe=False biar json_data yg berupa list bisa di serialize juga (klo safe=True yg bisa di serialize cuma dict aja)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        json_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'user': product.user.id if product.user else None,
        }      
        return JsonResponse(json_data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'not found'}, status=404)

@csrf_exempt
@require_POST
def add_product_by_ajax(request):
  
  name = strip_tags(request.POST.get("name"))
  price = request.POST.get("price")
  description = strip_tags(request.POST.get("description"))
  thumbnail = request.POST.get("thumbnail")
  category = request.POST.get("category")
  is_featured = request.POST.get("is_featured") == 'on'
  stock = request.POST.get("stock")
  brand = request.POST.get("brand")
  user = request.user
  
  newProduct = Product(
    name = name,
    price = price,
    description = description,
    thumbnail = thumbnail,
    category = category,
    is_featured = is_featured,
    stock = stock,
    brand = brand,
    user = user,
  )
  
  newProduct.save()
    
  return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def update_product_by_ajax(request):
  
  updatedData = json.loads(request.body)

  updatedProduct = Product.objects.get(pk=updatedData.get("id"))
  
  updatedProduct.name = strip_tags(updatedData.get("name"))
  updatedProduct.price = updatedData.get("price")
  updatedProduct.description = strip_tags(updatedData.get("description"))
  updatedProduct.thumbnail = updatedData.get("thumbnail")
  updatedProduct.category = updatedData.get("category")
  updatedProduct.is_featured = updatedData.get("is_featured") == 'on'
  updatedProduct.stock = updatedData.get("stock")
  updatedProduct.brand = updatedData.get("brand")
  updatedProduct.user = request.user
  
  updatedProduct.save()
    
  return HttpResponse(b"UPDATED", status=200)
    
def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
# def show_json_by_id(request, product_id):
#     try:
#         product_list = Product.objects.filter(pk=product_id)
#         json_data = serializers.serialize("json", product_list)
#         return HttpResponse(json_data, content_type="application/json")
#     except Product.DoesNotExist:
#         return HttpResponse(status=404)