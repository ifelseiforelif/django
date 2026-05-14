#from typing import Dict,Union
import json
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Product

def test(request:HttpRequest):
   # Product.objects.create(title="milk", price=140)
    # product = Product(title="bananas", price=73)
    # product.save()
    #products = Product.objects.all()
    # for product in products:
    #     print(product.title)
    #product = Product.objects.get(id=3)
    # print(product)
    #SELECT * FROM products WHERE title="limes" AND price=170
    #product = Product.objects.filter(price__gt=70) # >
    #product = Product.objects.filter(price__gte=70) # >=
    #product = Product.objects.filter(price__lt=100) # <
    #product = Product.objects.filter(price__lte=100) # <=
    #product = Product.objects.filter(price__lte=100) # <=
    #SELECT * FROM products WHERE title LIKE '%n%'
    #product = Product.objects.filter(title__contains="li") # реєстрозалежна перевірка
    #product = Product.objects.filter(title__icontains="Li") # НЕ реєстрозалежна перевірка
    #product = Product.objects.filter(Q(title="limes")|Q(price__gt=70))#OR
    #product = Product.objects.last()
    #product = Product.objects.first()
    #product = Product.objects.order_by("price") # asc
    #product = Product.objects.order_by("-price") # desc
    # SELECT * FROM products WHERE price IN [60,70,100]
    #product = Product.objects.filter(price__in=[60,70,140]).order_by("price")
    product = Product.objects.all().order_by("-id")[:2]  # LIMIT, TOP  
    print(product)
    return HttpResponse("Success")


@csrf_exempt
def home(request:HttpRequest):
    if request.method=='GET':
        
        # name:str|None = request.GET.get("name")
        # age:str|None =  request.GET.get("age")
        # data:Dict[str, Union[str, int|None]] = {
        #     "name":name,
        #     "age":age
        # }
        # SELECT * FROM myapp_post;
        posts = Post.objects.all()
        return render(request, 'home.html', {"data":posts})
    elif request.method=='POST':
       body = json.loads(request.body)
       title = body.get("title")
       post = Post(title=title)
       post.save()
       #Post.objects.create(title=title)
       return JsonResponse({"title":title}, status=201) # type: ignore

def contacts(request:HttpRequest):
    return render(request, 'contacts.html')
    #return HttpResponse("Contacts")

def about(request:HttpRequest):
      return render(request, 'about.html')
    #return HttpResponse(f'About {id}')

