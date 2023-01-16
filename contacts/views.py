from django.shortcuts import render, redirect, get_object_or_404

from .models import Contact, PhoneNumber


def create_contact_with_numbers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        numbers = request.POST.getlist('number')

        contact = Contact.objects.create(name=name)
        for number in numbers:
            PhoneNumber.objects.create(number=number, contact=contact)
            return redirect('contact-list')
    else:
        return render(request, 'create_contact.html')


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})
