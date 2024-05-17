from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.utils import translation
from django.contrib.sites.requests import RequestSite
from .models import TermsOfService, PrivacyPolicy
from django.template import loader
from .forms import ContactForm, ApplyNowForm
from django.core.mail import send_mail, get_connection, EmailMessage
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST

def home_page_view(request):
    term_of_services = TermsOfService.objects.all()
    privacy_policy = PrivacyPolicy.objects.all()
    return render(request, 'index.html',{
        'term_of_services': term_of_services,
        'privacy_policy': privacy_policy})

def apply_now(request):
    term_of_services = TermsOfService.objects.all()
    privacy_policy = PrivacyPolicy.objects.all()
    return render(request, 'applynow.html', {
        'term_of_services': term_of_services,
        'privacy_policy': privacy_policy})


def apply_now_success(request):
    term_of_services = TermsOfService.objects.all()
    privacy_policy = PrivacyPolicy.objects.all()
    return render(request, 'applynowsuccess.html', {
        'term_of_services': term_of_services,
        'privacy_policy': privacy_policy})



from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

def send_contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email message
            email_subject = 'Contact Form Web Page'
            email_message = f"From: {name}\nEmail: {email}\n\n{message}"

            try:
                # Send email using Gmail SMTP
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_RECEIVER],
                    fail_silently=False,
                )
                return render(request, 'contactussuccess.html')
            except Exception as e:
                # Handle exceptions during email sending
                print(f"Error sending email: {str(e)}")
                return render(request, 'index.html', {'form': form, 'error': str(e)})
    else:
        form = ContactForm()
    return render(request, 'index..html', {'form': form})

def contactussuccess(request):
    term_of_services = TermsOfService.objects.all()
    privacy_policy = PrivacyPolicy.objects.all()
    return render(request, 'contactussuccess.html', {
        'term_of_services': term_of_services,
        'privacy_policy': privacy_policy})

class SetLanguageView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        response = super().get_redirect_url(*args, **kwargs)
        if self.request.method == 'POST':
            language = self.request.POST.get('language')
            if language:
                request = self.request
                translation.activate(language)
                request.session[translation.LANGUAGE_SESSION_KEY] = language
        return response

@method_decorator(require_POST, name='dispatch')
class SetLanguageAndRedirectView(SetLanguageView):
    def get_redirect_url(self, *args, **kwargs):
        redirect_to = self.request.POST.get('next', '/')
        return super().get_redirect_url(*args, **{'to': redirect_to})