from django.contrib import admin

from .models import ParticipationApplication, Reiting, Uslugs, Zaiavki, Workers, Zakaz, Kater, Remont


class CourseAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(ParticipationApplication)
admin.site.register(Reiting)
admin.site.register(Uslugs)
admin.site.register(Zaiavki)
admin.site.register(Workers)
admin.site.register(Zakaz)
admin.site.register(Remont)
admin.site.register(Kater)