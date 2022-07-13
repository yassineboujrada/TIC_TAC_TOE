from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegistreform,gamer_login
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):

    # if request.user.is_authenticated():
    #     return HttpResponseRedirect("/game/")
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request,user)
            # c = Authentification_for_PowerBI().CLIENT_POWER_BI.
            # print('-------------------')
            # print(c)
            return redirect('game_blog-user')
            # return redirect('game_blog-game')
        else: 
            messages.info(request,"Username or Password Incorrect !")

    return render(request,'blog/login.html', {
        
    })

def besselama(request):
    logout(request)
    return redirect('game_blog-home')

@login_required
def game(request):
    return render(request,'blog/xo.html',{
        'play1':request.session['user1'],
        'play2':request.session['user2'],
    })

@login_required
def users(request):
    if request.method=="POST":
        request.session['user1']=request.POST.get("play1","")
        request.session['user2']=request.POST.get("play2","")
        return redirect('game_blog-game')
    return render(request,'blog/acceuil.html')

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

