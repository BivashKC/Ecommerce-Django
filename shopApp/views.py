from django.shortcuts import render
from .models import Clothes, Flags, Utensils

# Create your views here.
def clothesview(request):
    clothes = Clothes.objects.all().order_by('-id')
    c_context= {'clothes':clothes}
    return render(request, 'shopApp/clothes.html', c_context)


def flagview(request):
    flags = Flags.objects.all().order_by('-id')
    f_context= {'flags':flags}
    return render(request, 'shopApp/flags.html', f_context)


def utensilsview(request):
    utensils = Utensils.objects.all().order_by('-id')
    u_context= {'utensils':utensils}
    return render(request, 'shopApp/utensils.html', u_context)