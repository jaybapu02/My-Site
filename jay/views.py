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

        try:
            send_mail(
                "New Contact Form Submission",
                f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{desc}",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,   # VERY IMPORTANT
            )
        except Exception as e:
            print("Email failed:", e)
        messages.success(request, "Your message has been sent successfully!")
        return redirect('/contact/')

    return render(request, 'contact.html')