from django.contrib import admin
from ask_app import models
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title',)
class AnswerAdmin(admin.ModelAdmin):
    list_display=('text',)
admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.Answer,AnswerAdmin)