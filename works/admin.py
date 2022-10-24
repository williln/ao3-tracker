from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma

from works.models import Author, Work


class WordCountMixin:
    def words(self, obj):
        return intcomma(obj.word_count)


class WorksInline(WordCountMixin, admin.TabularInline):
    model = Work
    fields = ("title", "complete", "words")
    readonly_fields = ("title", "complete", "words")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("username", "url")
    search_fields = ("username",)
    readonly_fields = ("username", "url")
    inlines = [WorksInline]


class WorkAdmin(WordCountMixin, admin.ModelAdmin):
    date_hierarchy = "date_published"
    list_display = ("title", "author", "complete", "status", "words")
    list_filter = ("status", "complete")
    search_fields = ("author__username", "title")
    readonly_fields = ("url", "platform_id", "author", "title", "summary", "complete", "word_count", "date_published", "date_updated", "metadata")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Work, WorkAdmin)
