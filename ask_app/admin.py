from django.contrib import admin
from ask_app import models
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','text','author','tags')
class AnswerAdmin(admin.ModelAdmin):
    list_display=('text','author','tags')
admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.Answer,AnswerAdmin)