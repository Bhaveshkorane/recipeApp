from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def recipies(request):
    if request.method == "POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')

        var=recipes(recipe_name=recipe_name,recipe_image=recipe_image,recipe_description=recipe_description)
        var.save()
        return redirect('recipe_url')
    
    
    
    querryset=recipes.objects.all()

    if request.GET.get('search'):
        querryset=querryset.filter(recipe_name__icontains=request.GET.get('search'))
        print("search has begin")

    context={'rec':querryset}
    return render(request,'recipe.html',context)


def show_recipe(request):
    querryset=recipes.objects.all()

    if request.GET.get('search'):
        querryset=querryset.filter(recipe_name__icontains=request.GET.get('search'))
        print("search has begin")

    context={'rec':querryset}
    return render(request,'show.html',context)
    return HttpResponse("hello bhavesh")


def delete_recipe(request,id):

    querryset=recipes.objects.get(id= id)
    querryset.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

    #return redirect('/home/')

def update_recipe(request,id):

    querryset=recipes.objects.get(id=id)

    if request.method == "POST":
        data=request.POST

        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')

        if recipe_image:
            querryset.recipe_image=recipe_image

        querryset.recipe_name=recipe_name
        querryset.recipe_description=recipe_description
        querryset.save()

        return redirect('show_url') #working
        


    context={'rec':querryset}
    return render(request,'update.html',context)



def register(request):
    if request.method == 'POST':
        data=request.POST

        username=data.get('uname')
        first_name=data.get('fname')
        last_name=data.get('lname')
        email=data.get('Email')
        pass1=data.get('pass1')
        pass2=data.get('pass2')

        
        

        print(email)


        if(pass1 == pass2):
         if User.objects.filter(email=email).exists():
             messages.info(request,"the email alreday exist..")
             #return redirect('register_url')
         if User.objects.filter(username=username).exists():
             messages.info(request,"the username already exist...")
             #return redirect('register_url')
         else:
            user= User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=pass1,username=username)
            user.save()
            print("user created successfully")

        else:
            messages.info(request,"the password doesnt matches")


        redirect('register_url')

        
        context={'user':data}
        first_name=request.POST.get('first_name')

    return render(request,'register.html')
