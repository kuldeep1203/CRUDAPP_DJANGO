
from django.shortcuts import render,redirect
from .forms import habitatinsert
from django.contrib import messages
from django.contrib import admin
from .models import habitat
from django.shortcuts import get_object_or_404
admin.site.register(habitat)
def habitat_create(request):
    if request.method == 'POST':
        form = habitatinsert(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data inserted successfully!')
            return redirect('homehabitat')
    else:
        form = habitatinsert()
        #messages.error(request, 'Data inserted unsuccessfully!')
    return render(request, 'habitatinsert.html',{'form':form})

def homehabitat(request):
    return render(request,'homehabitat.html',{})

def habitat_search(request,pk):
    
        habitats_record=get_object_or_404(habitat,pk=pk)
        return render(request, 'habitat_record.html',{'habitats_record':habitats_record})

def habitat_record(request):
    habitat_list=habitat.objects.all()
    return render(request, 'homehabitat.html',{'habitat_list':habitat_list})

def habitat_Delete(request,pk):
    delete_it =get_object_or_404(habitat,pk=pk)
    delete_it.delete()
    messages.success(request,"Record deleted ..")
    return redirect('homehabitat')

def habitat_update(request,pk):
    current_record=get_object_or_404(habitat,pk=pk)
    form=habitatinsert(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated..")
        return redirect('homehabitat')
    return render(request, 'update_habitat.html',{'current_record':current_record,'form':form})
def search_habitat(request):
    if request.method =='POST':
        searched=request.POST['searched']
        filtered=request.POST['filter1']
        if filtered=='name':
            results=habitat.objects.filter(name__contains=searched)
            return render(request, 'searchhabitat.html',{'searched':searched, 'results':results})
        elif filtered=='major_fauna':
            results=habitat.objects.filter(major_fauna__contains=searched)
            return render(request, 'searchhabitat.html',{'searched':searched, 'results':results})
    else:
       
        return render(request, 'searchfauna.html',{})