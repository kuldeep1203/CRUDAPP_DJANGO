from django.shortcuts import render
from .models import Lineage
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import LineageForm
from django.contrib import messages
# Create your views here.
def lineage_update(request,pk):
    current_record=get_object_or_404(Lineage,animal_id_id=pk)
    form=LineageForm(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated..")
        return redirect('fauna')
    return render(request, 'update_lineage.html',{'current_record':current_record,'form':form})