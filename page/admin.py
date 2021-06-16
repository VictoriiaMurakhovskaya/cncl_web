from django.contrib import admin
from .models import Post, People, Contact, Member, Event, Order, PhotoView, Feedback

admin.site.register(People)
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(PhotoView)
admin.site.register(Feedback)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'date_time', 'title')