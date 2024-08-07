from django.shortcuts import render

def get_wellcome_home(request, *args, **kwargs):
    context = {
        "word": "amir"
    }
    
    return render(request,"home.html", context)
