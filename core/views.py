from django.shortcuts import render


def error_404(request, exception=None):
    return render(request, "errors/404.html", status=404)


def error_500(request):
    return render(request, "errors/500.html", status=500)


def error_404_demo(request):
    return error_404(request)


def error_500_demo(request):
    return error_500(request)
