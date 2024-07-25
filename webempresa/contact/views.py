from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    contact_form = ContactForm()
    

    if request.method =='POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviar correo y redirect
            email = EmailMessage(
                'Mente.energia | Gracias por tu mensaje',
                'De: {} {} \n\nEscribió:\n\n{}'.format(name, email,content),
                'mindsetclub19@outlook.com',
                ['mindsetclub19@outlook.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')
        

    return render(request, 'contact/contact.html', {'form':contact_form})