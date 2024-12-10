from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class CourseVideoInline(admin.TabularInline):
    model = CourseVideo
    extra = 1


class LessonVideoInline(admin.TabularInline):
    model = LessonVideo
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseVideoInline]


@admin.register(Lesson)
class LessonAdmin(TranslationAdmin):
    inlines = [LessonVideoInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Favorite)
admin.site.register(Cart)
admin.site.register(CartItem)



