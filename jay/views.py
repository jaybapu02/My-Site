from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from threading import Thread
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # 1️⃣ Save data to database
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        # 2️⃣ Send email to YOU (SendGrid)
        subject = "New Contact Form Submission"
        message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n\n"
            f"Message:\n{desc}"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,      # SendGrid verified email
            [settings.DEFAULT_FROM_EMAIL],    # You receive the mail
            fail_silently=False,
        )

        # 3️⃣ Success message
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'contact.html')
