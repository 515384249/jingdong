from django.shortcuts import render


# Create your views here.


def demo(request):
    context = {}
    return render(request, "demo.html", context)
def btstrap(request):
    context = {}
    return render(request, "jiaoda.html", context)

