from django.contrib import admin
from works.models import Author, Work


class AuthorAdmin(admin.ModelAdmin):
    pass


class WorkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Work, WorkAdmin)
