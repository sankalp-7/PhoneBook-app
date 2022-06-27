from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from . import models
# Create your views here.
def home(request):
    return render(request,'list/home.html')
class formview(CreateView):
    model=models.contactform
    fields="__all__"
    success_url="/view"
def ViewList(request):
    if 'srch' in request.GET:
        srch=request.GET['srch']
        contacts=models.contactform.objects.filter(first_name__icontains=srch)
    else:
        contacts=models.contactform.objects.all()
    dict={'contacts':contacts}
    return render(request,'list/contactform_list.html',context=dict)

class UpdateView(UpdateView):
    model=models.contactform
    fields="__all__"
    success_url="/view"
class DeleteView(DeleteView):
    model=models.contactform
    success_url="/view"


