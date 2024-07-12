from django.shortcuts import redirect, render,HttpResponse
from .models import *

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
