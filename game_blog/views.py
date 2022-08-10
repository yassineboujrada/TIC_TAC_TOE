from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        try:
            user=User.objects.get(username=username,password=password)
            login(request,user)
            return redirect('game_blog-user')
        except:
            messages.info(request,"Username or Password Incorrect !")

    return render(request,'blog/index.html', {
        
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

def register(request):
    if request.method=="POST":
        new_user=request.POST.get("usernme","")
        pass1=request.POST.get("pass1","")
        pass2=request.POST.get("pass2","")
        c=User.objects.filter(username=new_user)
        if not c:
            if pass1==pass2 and len(pass1)>=8:
                l=User(username=new_user,password=pass1)
                l.save()
                return redirect("game_blog-home")
            else:
                messages.success(request,"You're password and confirm password defferent or length not > 8")
                return redirect("registre")
        else:
            messages.success(request,"You're account already exist")
            return redirect("registre")
    return render(request,"blog/register.html")
