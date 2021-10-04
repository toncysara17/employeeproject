from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import EmployeeCreateForm,SigninForm
from django.urls import reverse_lazy
from .models import Employee,Login

# Create your views here.
def signin_view(request,*args,**Kwargs):
    form=SigninForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=SigninForm(request.POST)
        if form.is_valid():
            print("sucess")
            return redirect("home")
    return render(request,"login.html",context)



def home(request):
    return render(request,"home.html")

class EmpUpdateView(TemplateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = "update.html"
    context = {}

    def get(self, request, *args, **kwargs):
        employees = self.get_object(kwargs.get("id"))
        form = self.form_class(instance=employees)
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        employees = self.get_object(kwargs.get("id"))
        form = self.form_class(instance=employees, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")


class ViewEmp(DetailView):
    model = Employee
    template_name = "addemp.html"
    context_object_name = "employees"

class AddempView(CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = "addemp.html"
    success_url = reverse_lazy("home")



class EmpListView(ListView):
    model = Employee
    template_name = "list.html"
    context_object_name ="employees"


class UpdateEmpView(UpdateView):
    model = Employee
    template_name = "update.html"
    form_class = EmployeeCreateForm
    success_url = reverse_lazy("list")


class DeleteEmpView(DeleteView):
    model = Employee
    template_name = "delete.html"
    success_url = reverse_lazy("list")


class SignoutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return  redirect("signin")