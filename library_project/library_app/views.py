from django.shortcuts import render

# Create your views here.
def home(request):
    book1={'title': 'Book1', 'author': 'Author1', 'price':'500'}
    book2={'title': 'Book2', 'author': 'Author2', 'price':'800'}
    context={'book1': book1, 'book2': book2}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def books(request):
    books=[
        {'title': 'Book1', 'author': 'Author1', 'price':'500'},
        {'title': 'Book2', 'author': 'Author2', 'price':'500'},
        {'title': 'Book3', 'author': 'Author3', 'price':'700'}
    ]
    
    return render(request, 'books.html')