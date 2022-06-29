from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegistreform,gamer_login

def home(request):

    # if request.method=="POST":
    #     # form = UserLoginForm(request.POST)
    #     form=UserRegistreform(request.POST)
    #     # print("ok now here2")
    #     if form.is_valid(): 

    #         # print(form.cleaned_data['username'])

    #         return HttpResponseRedirect('/game/')
       
    # else:
    #     print("ooooooo")
    #     # form = UserLoginForm()
    #     form=UserRegistreform()

    # print("+++++++++++++++++++++++++++++++")

    form = UserRegistreform()
    if request.method=="POST":
        print(request.POST)
        form = UserRegistreform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/game/')

    return render(request,'blog/login.html',{'form':form})


def game(request):
    return render(request,'blog/xo.html')

# def register(request):
#     if request.method =="POST":
#         print("ok now here")
#         # form = UserCreationForm(request.POST)
#         form = UserRegistreform(request.POST)
#         print("ok now here2")
#         if form.is_valid():
#             form.save()
#             user=form.cleaned_data.get('username')
#             messages.success(request,f'Youre account has been  created {user}, Now you can login')
#             print("ok")
#             return redirect('login')
#     else:
#         print("not ok")
#         form = UserCreationForm()
#     print("+++++++++++++++++++++++++++++++")
#     return render(request,'users/register.html',{'form':form})

# Create your views here.

