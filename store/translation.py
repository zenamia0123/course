from .models import Lesson, Course, Assignment, Exam, Certificate
from modeltranslation.translator import TranslationOptions, register


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'description')