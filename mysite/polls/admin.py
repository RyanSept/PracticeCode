from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice,Question

class ChoiceInline(admin.TabularInline):
    model=Choice
    limit= 3
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text","pub_date","was_published_recently")
    list_filter= ["pub_date"]
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),
        ]
    search_fields= ["question_text","choice__choice_text"]
    inlines= [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
