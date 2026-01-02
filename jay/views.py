from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from django.conf import settings

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Save to database
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )
        contact.save()

        # Send email
        subject = "New Contact Form Submission"
        message = f"""
        You received a new contact request:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {desc}
        """

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['jaychandradasbapu05@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('/contact/')

    return render(request, 'contact.html')