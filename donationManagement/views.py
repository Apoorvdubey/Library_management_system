from django.shortcuts import render

# Create your views here.

def listDonations(request):
    return render(request, "donation/index.html", {})