from django.contrib import admin
from .models import Topic
from .models import Entry

# Register your models here.

admin.site.register(Topic) #manage our model thr. admin site
admin.site.register(Entry)