from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404

User = get_user_model()

@login_required
def profile_detail_view(request,username=None, *args, **kwargs):
    user = request.user
    profile_user_object = get_object_or_404(User, username=username)
    is_me = user == profile_user_object


    if user.has_perm('auth.user_view') or is_me: 
        context = {
            "object_user": profile_user_object
        }
        return render(request, "profiles/detail.html", context)
    
    else:
        raise Http404

@login_required
def profile_list_view(request, *args, **kwargs):
    user = request.user
    if user.has_perm('auth.user_view'):
        context = {
            "object_list": User.objects.filter(is_active=True)
        }
        return render(request, "profiles/list.html", context)
    raise Http404