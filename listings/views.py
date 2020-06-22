from django.shortcuts import render

# the def gets its method name from the urls.py .. ex: views.listing 
# Create your views here.
def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')