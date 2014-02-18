from django.shortcuts import render

from contentioussite.models import TextString


def index(request):
    context = {
        "text_string": TextString.objects.all()[0]
    }
    return render(request, "index.html", context)

