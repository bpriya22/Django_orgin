from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    # dest1=Destination()
    # dest1.name='Mumbai'
    # dest1.desc="The City that never Sleeps"
    # dest1.price= 700

    # dest2=Destination()
    # dest2.name="Mangalore"
    # dest2.desc = "A city of Beaches"
    # dest2.price=654

    # dest3=Destination()
    # dest3.name="Bangalore"
    # dest3.desc="The Silicon City of India"
    # dest3.price=890

    # dests=[dest1,dest2, dest3]    #we don't need all this..

    dests = Destination.objects.all()   #the above all commands are replaced by this one command.

    return render(request,"index.html",{'dests':dests})  #object created should be here.