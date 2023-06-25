from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Transfer
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import TransferForm
from django.contrib import messages
# Create your views here.
def transferupdate(request,pk):
    current_record=get_object_or_404(Transfer,animal_id_id=pk)
    form=TransferForm(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated..")
        return redirect('fauna')
    return render(request,'updatetransfer.html',{'current_record':current_record,'form':form})
