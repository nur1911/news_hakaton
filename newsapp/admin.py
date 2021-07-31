from django.contrib import admin


# Register your models here.
from newsapp.models import News_Details, Images, Filter, Language

admin.site.register(News_Details)
admin.site.register(Images)
admin.site.register(Filter)
admin.site.register(Language)