from django.shortcuts import render
# settings
from django.conf import settings

# Create your views here.
def index(request):
    context = {
        'title': 'Home Page',
    }

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'social/index.html', context=context)

