from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Comments
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mesg')
    list_filter = ('active', 'created_on')
