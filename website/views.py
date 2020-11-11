from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from .forms import ContactForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = form.cleaned_data['contact_email']
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            
            email = send_mail(
            "New contact form submission",
             content, 
             None, 
             ['daniel.morales117@yahoo.com'], 
             fail_silently=True)
            messages.success(request, "Message sent." )
            return redirect('home')
        else:
            form = ContactForm()
    return render(request, 'home.html', {'form': ContactForm})
