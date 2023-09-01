from django.contrib import admin
from .models import Category, Course, Lesson, SortingQuiz, CorrectAnswerQuiz, FreeTextQuiz, MultipleChoiceQuiz
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class CategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'slug', 'short_description')
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


class LessonInline(SortableStackedInline):
    model = Lesson
    extra = 0


class CourseAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('id', 'categories', 'title', 'slug', 'short_description', 'long_description', 'image', 'created_by',)
    readonly_fields = ('id',)
    list_filter = ('categories',)
    list_display = ('title', 'id', 'slug',)
    inlines = [LessonInline]


class SortingQuizAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'quiz_description', 'created_by', 'status', 'element1', 'element2', 'element3',
              'element4', 'element5', 'element6', 'element7', 'element8', 'element9', 'element10', 'element11',
              'element12',)
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


class CorrectAnswerQuizAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'quiz_description', 'created_by', 'status', 'correctAnswer', 'wrongAnswer1',
              'wrongAnswer2',)
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


class FreeTextQuizAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'quiz_description', 'created_by', 'status', 'correctAnswer1', 'correctAnswer2',
              'correctAnswer3', 'correctAnswer4', 'correctAnswer5',)
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


class MultipleChoiceQuizAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'quiz_description', 'created_by', 'status', 'answer1', 'solution1', 'answer2',
              'solution2', 'answer3', 'solution3', 'answer4', 'solution4', 'answer5', 'solution5',)
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(SortingQuiz, SortingQuizAdmin)
admin.site.register(CorrectAnswerQuiz, CorrectAnswerQuizAdmin)
admin.site.register(FreeTextQuiz, FreeTextQuizAdmin)
admin.site.register(MultipleChoiceQuiz, MultipleChoiceQuizAdmin)


