from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import HealthForm
from django.contrib import messages

from .models import Health
# Create your views here.
def health_update(request,pk):
    current_record=get_object_or_404(Health,animal_id_id=pk)
    form=HealthForm(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated..")
        return redirect('fauna')
    return render(request, 'update_fauna.html',{'current_record':current_record,'form':form})
   