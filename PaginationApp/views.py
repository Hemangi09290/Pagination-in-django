from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from PaginationApp.models import Contact
from django.views.generic import ListView

# Create your views here.
class ContactListView(ListView):
    queryset = Contact.objects.all()
    context_object_name = 'contacts'
    paginate_by = 2
    template_name = 'home_page.html'

def home(request):
    return HttpResponse("Hello, Django!")

def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})