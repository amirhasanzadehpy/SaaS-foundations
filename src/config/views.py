from django.shortcuts import render

def home_view(request, *args, **kwargs):
    context = {
        "word": "amir"
    }
    
    return render(request,"home.html", context)
