from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore

from .models import LongToShort

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    context = {
        "submitted": False,
        "error": False
    } # type: ignore

    if request.method == 'POST':
        

        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']


        try:
            object = LongToShort(long_url = long_url, short_url = custom_name)
            object.save()

            date = object.date
            clicks = object.clicks 

            print(long_url)
            print(custom_name)

            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context["date"] = date
            context["clicks"] = clicks
            context["submitted"] = True

        except:
            context["error"] = True

    else:
        print("User is not sending anything")

        

    return render(request, "index.html", context)


def redirect_url(request, short_url):
    row = LongToShort.objects.filter(short_url = short_url)

    if len(row) == 0:
        return HttpResponse("No such shorturl exists")
    
    object = row[0]
    long_url = object.long_url

    object.clicks = object.clicks + 1
    object.save()

    return redirect(long_url)

def all_analytics(request):

    rows = LongToShort.objects.all()

    context = {
        "rows": rows
    }

    return render(request, "all-analytics.html", context)
    