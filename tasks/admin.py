from django.contrib import admin
from .models import Task, TaskImage

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'is_complete', 'created_at', 'last_updated_at', 'user')
    list_filter = ('due_date', 'priority', 'is_complete', 'created_at')
    search_fields = ('title', 'description')

    def last_updated_at(self, obj):
        return obj.last_updated_at.strftime("%Y-%m-%d %H:%M:%S") if obj.last_updated_at else None

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'images')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskImage, ImageAdmin)
