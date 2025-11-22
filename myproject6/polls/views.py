from django.http import HttpResponse

def index(request):
    return HttpResponse("Salam, bu mənim öyrənmək üçün olan Django səhifəmdir!")

