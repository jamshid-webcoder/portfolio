from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def portfolio(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('portfolio')
    else:
        form = ContactForm()
    return render(request, 'index.html',)