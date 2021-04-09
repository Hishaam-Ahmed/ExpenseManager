from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ListName, Expense
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required


@login_required
def index(response, name):
    expense_list = ListName.objects.filter(user=response.user).get(name=name)

    if response.method == "POST":
        if response.POST.get("new"):
            new_expense = response.POST.get("newExpense")
            new_cost = response.POST.get("newCost")
            expense_list.expense_set.create(
                title=new_expense, cost=new_cost)

    return render(response, "finance/list.html", {"expense_list": expense_list})


def home(response):
    return render(response, "finance/home.html", {})


@login_required
def dashboard(request):
    lists = ListName.objects.filter(user=request.user)
    return render(request, "finance/dashboard.html", {"lists": lists})


@login_required
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ListName(name=n)
            t.save()
            response.user.listname.add(t)

        return HttpResponseRedirect("../dashboard")

    else:
        form = CreateNewList()

    return render(response, "finance/create.html", {"form": form})


def delete_list(response, name):
    expense_list = ListName.objects.get(name=name)

    if response.method == 'POST':
        expense_list.delete()

        return HttpResponseRedirect("../../")

    return render(response, "finance/delete.html", {"expense_list": expense_list})
