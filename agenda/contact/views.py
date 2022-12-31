from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request, letter = ''):
    """
    Purpose: request
    """
    contacts = Contact.objects.all()
    if letter != '':
        contacts = contacts.filter(name__istartswith = letter)
    
    search = request.GET.get('search', '')
    contacts = contacts.filter(
        name__contains=search).order_by('-id')
    
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','v','y','z']
    context = {
        'search': search,
        'contacts': contacts,
        'letters': letters
    }
    
    return render(request,
                  'contact/index.html',
                  context)
# end def


def view(request, id):
    """
    Purpose: request
    """
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context)
# end def


def edit(request, id):
    """
    Purpose: request
    """
    contact = Contact.objects.get(pk=id)
    if (request.method == 'GET'):
        contact_form = ContactForm(instance=contact)
        context = {
            'contact_form': contact_form,
            'id': id
        }
        return render(request, 'contact/edit.html', context)
    elif (request.method == 'POST'):
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
        context = {
            'contact_form': contact_form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado correctamente!')
        return render(request, 'contact/edit.html', context)
# end def


def create(request):
    """
    Purpose: request
    """
    if (request.method == 'GET'):
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form,
        }
        return render(request, 'contact/create.html', context)
    elif (request.method == 'POST'):
        contact_form = ContactForm(request.POST)
        if not contact_form.is_valid():
            context = {
                'contact_form': contact_form,
            }
            return render(request, 'contact/create.html', context)
        contact_form.save()
        return redirect('contact')
# end def

def delete(request, id):
    """
    Purpose: request
    """
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('contact')
# end def