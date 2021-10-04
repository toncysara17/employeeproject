from django.urls import path
from .views import signin_view,home,AddempView,EmpListView,UpdateEmpView,DeleteEmpView,SignoutView


urlpatterns=[
    path("login",signin_view,name="signin"),
    path("home",home,name="home"),
    path("addemp", AddempView.as_view(), name="addemp"),
    path("list",EmpListView.as_view(),name="list"),
    path("emp_project/edit/<int:pk>",UpdateEmpView.as_view(),name="update"),
    path("emp_project/delete/<int:pk>", DeleteEmpView.as_view(), name="delete"),
    path("signout", SignoutView.as_view(), name="signout"),

]