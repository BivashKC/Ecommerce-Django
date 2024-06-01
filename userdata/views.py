from django.shortcuts import render

# Create your views here.
def loginview(request):
    return render(request, 'userdata/login.html')

def signupview(request):
    return render(request, 'userdata/signup.html')