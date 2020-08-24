from django.shortcuts import render

# Create your views here.
def home(request):
    #do stuff with the request
    #save SOC and DOD to database
    

    return render(request, 'home.html', {})