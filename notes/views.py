from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from notes.models import UserProfile,Notes
from django.contrib import messages
from django.views.generic import View,CreateView,TemplateView,FormView
from notes.forms import UserProfileFrom,NotesForm,UserRegistrationForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate,logout

# Create your views here.

class CreateUserProfile(CreateView):
    model = UserProfile
    template_name = "registration.html"
    form_class = UserProfileFrom
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Profile has been created")
        self.object = form.save()
        return super().form_valid(form)

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration.html"
    model = User
    success_url = reverse_lazy("signin")

class LogInView(FormView):
    form_class=LoginForm
    template_name="login.html"
    model=User
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("name")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("success")
                return redirect("home")
            else:
                return render(request,self.template_name,{"form":form})



class CreateNotesView(CreateView):
    model = Notes
    template_name = "home.html"
    form_class = NotesForm
    success_url = reverse_lazy ("home")
    def form_valid(self, form):
        messages.success(self.request,"Notes created successfully")
        self.object = form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)


class ViewMyNotes(TemplateView):
    template_name = "view-notes.html"




