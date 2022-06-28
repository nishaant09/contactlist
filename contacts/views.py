from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})

def addContact(request):
    if request.method == 'POST':

        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address'],
            )
        new_contact.save()
        return render(request, 'index.html')
        
      

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        Contact.full_name = request.POST['fullname']
        Contact.relationship = request.POST['relationship']
        Contact.email = request.POST['email']
        Contact.phone_number = request.POST['phone-number']
        Contact.address = request.POST['address']
        Contact.save()
        
        return redirect('/profile/'+str(Contact.id))
    return render(request, 'edit.html', {'contacts': Contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contacts': contact})

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contacts':contact})

        












    

