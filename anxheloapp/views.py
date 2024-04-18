from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
class HomePageView(TemplateView):
    template_name = "index.html"







def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email message
            email_message = f"From: {name}\nEmail: {email}\n\n{message}"

            # Send email using Gmail SMTP
            send_mail(
                subject='Contact Form Submission',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_RECEIVER],
                fail_silently=False,
            )
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
