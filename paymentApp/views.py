from django.shortcuts import render

# Create your views here.
def paymentview(request):
    return render(request, 'paymentApp/payment.html')