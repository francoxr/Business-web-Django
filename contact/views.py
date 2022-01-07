from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            print('aqui')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # send a email and redirect
            email = EmailMessage(
                'La caffettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ["franco.roca.pe@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                # Fail
                return redirect(reverse('contact')+"?fail")
            # all good 
            return redirect(reverse('contact')+"?ok")

    return render(request, "contact/contact.html", {'form': contact_form})