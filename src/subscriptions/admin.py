from django.contrib import admin
from .models import Subscriptions, UserSubscription

admin.site.register(Subscriptions)
admin.site.register(UserSubscription)
