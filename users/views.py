from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm




#if we get a post request that is submition of data from the form 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #sending flash msg if data is valid
            #messages.success(request,f'Account created , you can now login!')
            #remember to add the messages on the logged in screen or home screen acturally 
            #{%if messages %} {%for message in messages%}{%endfor%} div class =alert alert -{{message.tag}} end if
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def homepage(request):
   return render(request,"front\\templates\\h.html")