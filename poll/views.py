from django.shortcuts import render
from django.http import HttpResponse

from .forms import PollForm 

# Create your views here.
def poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        context = {
            'form' : form
        }
        return render(request, 'poll/poll.html', context)
    else:
        form = PollForm()
        context = {
            'form' : form
        }
        return render(request, 'poll/poll.html', context)