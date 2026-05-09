#from typing import Dict,Union
import json
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post

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
       body:str|bytearray|bytes = json.loads(request.body)

       return JsonResponse({"name":body.get("name"), "email":body.get("email")}, status=201) # type: ignore

def contacts(request:HttpRequest):
    return render(request, 'contacts.html')
    #return HttpResponse("Contacts")

def about(request:HttpRequest):
      return render(request, 'about.html')
    #return HttpResponse(f'About {id}')