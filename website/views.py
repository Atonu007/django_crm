from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):


    #check if user is logging in
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        

        # authenticate
        user = authenticate(request, username=user_name, password=password)
        
        
        if user is not None:
            
            login(request,user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        
        else:
            messages.success(request,'Error try Again later')
            return redirect('home')
    else:
        return render(request,'home.html', {})





def logout_user(request):
    logout(request)
    messages.success(request,'You Have been logged Out')
    return redirect('home')
