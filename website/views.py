from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.
def home(request):

    records = Record.objects.all()


    #check if user is logging in
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        

        # authenticate
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            
            login(request,user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        
        else:
            messages.success(request,'Error try Again later')
            return redirect('home')
    else:
        return render(request,'home.html', {'records':records})





def logout_user(request):
    logout(request)
    messages.success(request,'You Have been logged Out')
    return redirect('home')


def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Corrected: added parentheses to is_valid method
            user = form.save()  # Save the form data and get the user object

            # Authenticate user after registration
            username = form.cleaned_data['username']  # Corrected: changed parentheses to square brackets
            password = form.cleaned_data['password1']  # Corrected: changed parentheses to square brackets

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully')
            return redirect('home')
    else:
        form = SignUpForm()  # Corrected: added parentheses to instantiate the form

    return render(request, 'register.html', {'form': form})




def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
      
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')




def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')