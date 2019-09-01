from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


