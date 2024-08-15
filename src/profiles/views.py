from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

User = get_user_model()

@login_required
def user_detail_view(request,username=None, *args, **kwargs):
    user = request.user
    print(user.has_perm('auth.view_user'))
    profile_user_object = get_object_or_404(User, username=username)
    is_me = user == profile_user_object

    return HttpResponse(f"user is {username}, id: {profile_user_object.id}, {is_me}")


@login_required
def user_list_view(request, *args, **kwargs):
    pass