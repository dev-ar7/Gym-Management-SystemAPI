from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.register(User)
admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Plan)
admin.site.register(Member)
admin.site.unregister(Group)