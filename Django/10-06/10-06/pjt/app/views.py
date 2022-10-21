from multiprocessing import context
from django.shortcuts import render,redirect
from . models import App
from .forms import AppForms

# Create your views here.


def index(request):
    apps = App.objects.order_by('-pk')
    context = { 
               'apps' : 'apps'          
}
    return render(request, 'apps/index.html', context)

def new(request):
    app_form = AppForms()
    context = {
        'app_form' : app_form
    }
    
    return render(request, 'apps/new.html',context=context)

def create(request):
    app_form = AppForms(request.POST)
    if app_form.is_vaild():
        app_form.save()
        return redirect('app:index')
    else: 
        context = {
            'app_form' :app_form
        }
        return render(request, 'app/new.html',context=context)
    
    
def detail(request,pk):
    
    app = App.objects.get(pk=pk)
    context = {
        'app':app
    }
    return render(request, 'app/detail.html', context)

def update(request,pk):
    
    app = App.objects.get(pk=pk)
    app_form = AppForms(instance=app)
    context = {
        'app_form: app_form'
    }
    return render(request, 'app/update.html', context)