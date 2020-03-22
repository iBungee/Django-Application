from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User

# Create your models here.
class Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"

        

class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    isAvailable = models.BooleanField()

    def __str__(self):
        return f"user:{self.user}, date:{self.date}, isAvailable:{self.isAvailable}"        


def create_availability(sender, **kwargs):
    print(f"create_availability - sender={sender}, kwargs={kwargs}")
    if kwargs['created'] == True:
        date = kwargs['instance']
        print(f"date: {date}")
        for user in User.objects.all():
            print(f"user: {user}")
            availability = Availability(user=user, date=date, isAvailable=False)
            print(f"availability: {availability}")
            availability.save()
        return

post_save.connect(create_availability, sender=Date)