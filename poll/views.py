from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.contrib import messages
from django.contrib.auth.models import User


register = template.Library()

from .models import Availability, Date

# Create your views here.
def poll(request): # WSGIRequest

    print(f"{request.POST}")

    if request.method == 'POST':
        return _poll_post(request)
    else:
        return _poll_get(request)

def _poll_get(request):
    dates = Date.objects.all()
    pollInfo = dict()
    for date in dates:
        pollInfo[date] = Availability.objects.filter(date=date)
    context = {'pollInfo' : pollInfo}
    return render(request, 'poll/poll.html', context)

def _poll_post(request):
    if request.POST.get("submit"):
        _poll_post_submit(request)
        
    elif request.POST.get("newDate"):
        _poll_post_date(request)

    elif request.POST.get("newUser"):
        _poll_post_user(request)

    return _poll_get(request)

def _poll_post_submit(request):
    def update_availability(users_availability: Availability, isAvailable: bool):
        if users_availability.isAvailable != isAvailable:
            users_availabilities.filter(pk=users_availability.pk).update(isAvailable = isAvailable)
        return
        
    availability = Availability.objects.all()
    # Users: QuerySet of user foreign keys e.g. [1,2,3]
    users = availability.values_list('user', flat=True).distinct()
    # print(f"users: {users}")
    for user in users:
        # users_availabilities: QuerySet of Availability
        users_availabilities = availability.filter(user=user)
        print(f"users_availabilities: {users_availabilities}")
        for users_availability in users_availabilities:
            # print(f"users_availability: {users_availability}")
            listOfAvailabileDates = request.POST.getlist(str(users_availability.user))
            if listOfAvailabileDates:
                # print(f"gLIST {type(listOfAvailabileDates)}: {listOfAvailabileDates}")
                # print(f"{type(users_availability.date)} {users_availability.date}")

                if str(users_availability.date) in listOfAvailabileDates:
                    update_availability(users_availability, True)
                else:
                    update_availability(users_availability, False)
    return

def _poll_post_date(request):
    dateString: str = request.POST.get("date")
    if Date.objects.filter(date=dateString):
        # Date already exist
        messages.warning(request, f'Date already exists')
    else:
        # Date.objects.create()
        date = Date(date = dateString)
        date.save()
    return

def _poll_post_user(request):
    name = request.POST.get("username")
    if User.objects.filter(username=name):
        # User already exist
        messages.warning(request, f'User already exists')
    else:
        # Create users
        # Queryset.get_or_create()
        pass
    return