from django.contrib import admin

from .models import Course, ParticipationApplication, Reiting, Uslugs, Zaiavki, Workers, Zakaz


class CourseAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(ParticipationApplication)
admin.site.register(Reiting)
admin.site.register(Uslugs)
admin.site.register(Zaiavki)
admin.site.register(Workers)
admin.site.register(Zakaz)