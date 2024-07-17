from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')
def result(request):
    return render(request, 'result.html')