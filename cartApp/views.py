from django.shortcuts import render

# Create your views here.
def clothes_cartview(request):
    return render(request, 'cartApp/clothes_cart.html')

def flag_cartview(request):
    return render(request, 'cartApp/flag_cart.html')

def utensils_cartview(request):
    return render(request, 'cartApp/utensils_cart.html')