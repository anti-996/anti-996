from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Company

from .forms import CompanyForm

# Create your views here.


def company_list(request: HttpRequest):
    ctype = request.GET.get("ctype", "1")
    try:
        ctype = int(ctype)
    except Exception:
        ctype = 1
    companies = Company.objects.all().filter(ctype=ctype)
    paginator = Paginator(companies, 6)
    page = request.GET.get("page", 1)
    try:
        p = page
    except PageNotAnInteger:
        p = 1
    except EmptyPage:
        p = paginator.num_pages

    print("page is %s, p is %s" % (page, p))
    return render(request, "company/list.html", {"companies": paginator.page(p), "ctype": ctype})


def company_detail(request: HttpRequest, pk):
    company = get_object_or_404(Company, pk=pk)
    
    return render(request, "company/detail.html", {"company": company})


def company_add(request: HttpRequest):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = CompanyForm()
    return render(request, 'company/add.html', {'form': form})


def thanks(request: HttpRequest):

    return render(request, "thanks.html")

