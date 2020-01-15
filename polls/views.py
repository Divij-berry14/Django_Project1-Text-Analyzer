from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!.")
def polls1(request):
    return HttpResponse("Hello, This is Polls1 Page!")