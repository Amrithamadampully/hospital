from django.shortcuts import render

# Create your views here.
def logo(request):
    return render(request,'logo.html')
