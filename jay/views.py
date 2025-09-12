from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        desc = request.POST.get("desc", "").strip()

        # Check if required fields are empty
        if not name or not email or not desc:
            messages.warning(request, "⚠ Please fill all required fields before submitting!")
            return redirect("contact")

        # Save into database
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

        messages.success(request, f"✅ Thank you {name}! Your message has been sent.")
        return redirect("contact")

    return render(request, "contact.html")
