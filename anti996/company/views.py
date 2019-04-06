from django.shortcuts import render
from django.http.request import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Company

# Create your views here.


def company_list(request: HttpRequest):
    companies = Company.objects.all().filter(ctype=Company.GOOD)
    paginator = Paginator(companies, 10)
    page = request.GET.get("page", 1)
    try:
        p = page
    except PageNotAnInteger:
        p = 1
    except EmptyPage:
        p = paginator.num_pages

    print("page is %s, p is %s" % (page, p))
    return render(request, "company/list.html", {"companies": paginator.page(p)})
