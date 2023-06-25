from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import animalsinsert
from django.db import connection, transaction
from datetime import date
from lineage.models import Lineage
from health.models import Health
from django.contrib import messages
from .models import animals
from django.contrib import admin
from datetime import datetime
from .forms import animalsinsert
from migration.models import AMigrations
from transfers.models import Transfer

# Create your views here.
admin.site.register(animals)
cursor = connection.cursor()

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year
    # Check if the birthday has already occurred this year
    if today < date(today.year, dob.month, dob.day):
        age -= 1
    return age
def animals_insert(request):
    if request.method == 'POST':
        form = animalsinsert(request.POST)
        if form.is_valid():
            form.save() # Save the form data without committing to the database
            

            return redirect('fauna')
    else:
        form = animalsinsert()
    
    return render(request, 'insert.html', {'form': form})

def fauna(request):
    animal_list=animals.objects.all()
    return render(request, 'fauna.html',{'animal_list':animal_list})

def animals_record(request,pk):
        Migration_records = AMigrations.objects.filter(animal_id_id=pk)
        Lineage_records = Lineage.objects.filter(animal_id_id=pk)
        health_records = Health.objects.filter(animal_id_id=pk)
        animals_record=get_object_or_404(animals,pk=pk)
        Transfer_records=Transfer.objects.filter(animal_id_id=pk)
        return render(request, 'animal_record.html',{'Transfer_records': Transfer_records,'Migration_records':Migration_records,'Lineage_records':Lineage_records,'health_records':health_records, 'animals_record':animals_record})
    
def animals_delete(request,pk):
    delete_it =get_object_or_404(animals,pk=pk)
    delete_it.delete()
    messages.success(request,"Record deleted ..")
    return redirect('fauna')
def animals_update(request,pk):
    current_record=get_object_or_404(animals,pk=pk)
    form=animalsinsert(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated..")
        return redirect('fauna')
    return render(request, 'update_fauna.html',{'current_record':current_record,'form':form})
    
def search_fauna(request):
    if request.method =='POST':
        searched=request.POST['searched']
        filtered=request.POST['filter']
        if filtered=='name':
            results=animals.objects.filter(aname__contains=searched)
            return render(request, 'searchfauna.html',{'searched':searched, 'results':results})
        #results=animals.objects.filter(animal_id__icontains=searched)
        elif filtered=='dob':
            do=request.POST['datepicker']
            try:
                selected_date = datetime.strptime(do, '%Y-%m-%d')
                results = animals.objects.filter(dob__contains=selected_date.date())
                return render(request, 'searchfauna.html', {'do': do, 'results': results})
            except ValueError:
                messages.error(request, "Invalid date format. Please select a valid date.")
                return render(request, 'searchfauna.html', {})

        elif filtered=='doa':
            do=request.POST['datepicker']
            try:
                selected_date = datetime.strptime(do, '%Y-%m-%d')
                results = animals.objects.filter(date_of_arrival__contains=selected_date.date())
                return render(request, 'searchfauna.html', {'do': do, 'results': results})
            except ValueError:
                messages.error(request, "Invalid date format. Please select a valid date.")
                return render(request, 'searchfauna.html', {})
        elif filtered=='species':
           
           
            results=animals.objects.filter(specices__contains=searched)
            return render(request, 'searchfauna.html',{'searched':searched, 'results':results})
        elif filtered=='gender':
           
           
            results=animals.objects.filter(sex__contains=searched)
            return render(request, 'searchfauna.html',{'searched':searched, 'results':results})
        elif filtered=='habitat':
           
           
            results=animals.objects.filter(Habitat_id__name__contains=searched)
            return render(request, 'searchfauna.html',{'searched':searched, 'results':results})


        else:
            messages.success(request,"No record found..")
            return render(request, 'searchfauna.html',{})
           
    
        #return render(request, 'searchfauna.html',{'searched':searched,'results':results})
    else:
       
        return render(request, 'searchfauna.html',{})
    




""" filters=request.GET.get('filters')
        #reuslts=animals.objects.all()
        if filters == 'Name':
            results = animals.objects.filter(aname__icontains=searched)
        elif filters == 'Species':
            results = animals.objects.filter(specices__icontains=searched)
        elif filters == 'Date of Birth':
            results = animals.objects.filter(dob=searched)
        elif filters == 'id':
            results=animals.objects.filter(animal_id=int(searched))
        elif filters == 'Date of arrival':
            results=animals.objects.filter(date_of_arrival=searched)
        else:
            messages.success(request,"Select  a filter")
                    
        elif filtered=='age':
            results=animals.objects.filter(age__contains=searched
            return render(request, 'searchfauna.html',{'searched':searched, 'results':results})

 """
