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

    
    return render(request,'index.html')

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
        return redirect('/')


    return render(request, 'new.html')
    
    

        












    

