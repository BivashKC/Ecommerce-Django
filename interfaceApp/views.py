from django.shortcuts import render, redirect
from .models import Contact

def homeview(request):
    return render(request, 'interfaceApp/home.html')

def contactview(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        contact_number = request.POST.get('contact_number')
        order_message = request.POST.get('order_message')

        # Save to database
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            state=state,
            city=city,
            zip_code=zip_code,
            contact_number=contact_number,
            order_message=order_message
        )

        return redirect('home')  # Redirect to a success page or home page

    return render(request, 'interfaceApp/contact.html')

def aboutview(request):
    return render(request, 'interfaceApp/about.html')
