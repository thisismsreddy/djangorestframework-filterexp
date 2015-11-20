from django.contrib import admin

# Register your models here.
from quickstart.models import *

admin.site.register(Tag)
# admin.site.register(User)
admin.site.register(Following)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Like)