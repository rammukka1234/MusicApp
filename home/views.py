from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def telugu(request):
    return render(request,'telugu.html')
def hindi(request):
    return render(request,'hindi.html')
def english(request):
    return render(request,'english.html')
def about(request):
    return render(request,'about.html')
