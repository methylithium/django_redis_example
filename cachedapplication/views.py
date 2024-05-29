from django.shortcuts import render
from .models import Programmer
from django.views.decorators.cache import cache_page

@cache_page(60*15)
def home(request):

    programmers = Programmer.objects.all()

    context = {
        'programmers': programmers
    }

    return render(request, 'list_all.html', context)