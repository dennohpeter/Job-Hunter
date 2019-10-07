import pprint
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Welcome you are at job hunter homepage.</h4>", status=200)


