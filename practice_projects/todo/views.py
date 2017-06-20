from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone

def todo_home(request):
    order_by = request.GET.get('order_by','')
    if order_by:
        return render(request,"todo/home.html",{'Task':Task.objects.all().order_by(order_by)})
    else:
        return render(request,"todo/home.html",{'Task':Task.objects.all()})

def edit_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    form = TaskForm(instance=task)
    context= {
        'form':form,
        'Task':task
        }
    if request.method == "POST":
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            task_form=TaskForm(request.POST, instance=task)
            task_form.save()
            return HttpResponseRedirect(reverse('todo_home'))
            
    return render(request,"todo/edit.html",context)

def create_task(request):
    form=TaskForm()
    context= {
        'form':form,
        }
    if request.method == "POST":
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            creation = task_form.save(commit=False)
            creation.creation_date = timezone.now()
            creation.save()
            return HttpResponseRedirect(reverse('todo_home'))
        
    return render(request,"todo/edit.html",context)

def delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('todo_home'))
