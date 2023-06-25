
from django.shortcuts import render
from .models import AMigrations
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import AMigrationsForm
from django.contrib import messages
# Create your views here.
def migration_update(request,pk):
    current_record=get_object_or_404(AMigrations,animal_id_id=pk)
    form=AMigrationsForm(request.POST or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated..")
        return redirect('fauna')
    return render(request, 'update_migration.html',{'current_record':current_record,'form':form})
