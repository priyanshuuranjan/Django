from django.shortcuts import render,HttpResponse

# Create your views here.
def recipe_list(request):
    return HttpResponse('List of recipes')

def recipe_detail(request,recipe_id):
    return HttpResponse(f'details of recipe # {recipe_id}')

def category_list(request):
    return HttpResponse('List of categories')

def category_detail(request,category_id):
    return HttpResponse(f'Details for the category : {category}')