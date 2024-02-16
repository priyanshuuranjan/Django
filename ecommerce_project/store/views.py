from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request,'about.html',{'title':'About'})
def products(request):
    products_data=[
        {'name':'product1','price':78.45},
        {'name':'product2','price':45.45},
        {'name':'product3','price':99.45},
    ]
    return render(request,'products.html')
