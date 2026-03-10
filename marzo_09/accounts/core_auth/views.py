from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class CustomLoginViews(LoginView):
    template_name = "core_auth/login.html"
    redirect_authenticated_user=True
    success_url=reverse_lazy("core_auth:profile")

    #def get_success_url(self):
    #    return "core_auth:profile"
        #return self.request.GET.get("next") or reverse_lazy("core_auth:profile")
    
class CustomLogoutView(LogoutView):
    pass

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save() # aca es cuando se dispara el SIGNAL
            login(request,user)
            messages.success(request,"Tu cuenta ha sido creada correctamente")
            return redirect("core_auth:profile")
    else:
        form=RegisterForm()

    context={
        'form':form,
    }
    return render(request,"core_auth/register.html",context=context)

@login_required
def profile_view(request):
    return render(request,"core_auth/profile.html")

@login_required
def profile_edit_view(request):
    profile=request.user.profile
    created=False

    if request.method=="POST":
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Tu perfil ha sido actualizado correctamente")
            return redirect("core_auth:profile")
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=profile)

    context={
        "user_form":user_form,
        "profile_form":profile_form,
    }
    return render(request,"core_auth/profile_edit.html",context=context)