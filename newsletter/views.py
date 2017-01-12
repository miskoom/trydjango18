from django.conf import settings 
from django.core.mail import send_mail 
from django.shortcuts import render

from  .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = 'SignUp Now'
    form= SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        fullname = form.cleaned_data.get("fullname")
        if not fullname:
            fullname = "new fullname"
        instance.fullname = fullname
        # if not instance.fullname:
        #   instance.fullname = "Miskoom"
        instance.save()
        context= {
            "title": "Thank You"
        }

    if request.user.is_authenticated() and request.user.is_staff:
        context = {
        "queryset": [123, 456]
        }

    
    return render (request, "home.html", context)



def contact(request):
    title = "Contact Us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_fullname = form.cleaned_data.get("fullname")

        subject= " Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, "yourotheremail@gmail.com"]
        contact_message = "%s: %s via %s" %(
            form_fullname, 
            form_message, 
            form_email)
        
        send_mail(subject,
                 contact_message, 
                 from_email, 
                 [to_email], 
                 fail_silently=False)

    context = {
        "form":form,
        "title": title,
        "title_align_center": title_align_center,

    }
    return render (request, "forms.html", context)