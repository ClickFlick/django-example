from django.shortcuts import render
from home import forms
from .forms import NewOrder,SponsorContact
from django.core.mail import send_mail
from OS2.settings import *
# Create your views here.


def index(request):
    return render(request,'homeland/index.html')


def test(request):
    return render(request, 'homeland/test.html')


def buy(request):
    return render(request, 'homeland/buy.html')


def contact(request):
    form = SponsorContact
    if request.method == "POST":
        form = SponsorContact(request.POST)
        if form.is_valid():
            subject = 'OS Project'
            name = form.cleaned_data.get('name')
            message = 'Thank you for reaching out to us,' + name + ' you will soon be contacted from your email address'
            from_email = EMAIL_HOST_USER
            to_email = [form.cleaned_data.get('email')]
            send_mail(subject, message,from_email, to_email, fail_silently=False)
            form.save()
            return index(request)
        else:
            print("ERROR")
    return render(request, 'homeland/contact.html', {'form': form})


def about(request):
    return render(request, 'homeland/about.html')


def property_det(request):
    form = NewOrder()

    if request.method == "POST":
        form = NewOrder(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")
    return render(request, "homeland/property-details.html", {"form": form})


def list_view(request):
    return render(request, 'homeland/view-list.html')



