from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from threading import Thread
from .models import Contact


def send_contact_email(subject, message, from_email, recipient_list):
    """
    Send email in background to avoid blocking / memory kill on Render
    """
    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=True,
        )
    except Exception as e:
        print("Email failed:", e)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # 1️⃣ Save to database (SAFE)
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        # 2️⃣ Send email in background (NON-BLOCKING)
        email_subject = "New Contact Form Submission"
        email_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n\n"
            f"Message:\n{desc}"
        )

        Thread(
            target=send_contact_email,
            args=(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
            )
        ).start()

        # 3️⃣ User feedback
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # use URL name

    return render(request, 'contact.html')
