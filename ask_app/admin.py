from django.contrib import admin
from ask_app import models
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title',)
class AnswerAdmin(admin.ModelAdmin):
    list_display=('text',)
class TagAdmin(admin.ModelAdmin):
    list_display=('tag',)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('login',)

admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.Answer,AnswerAdmin)
admin.site.register(models.Tag,TagAdmin)
admin.site.register(models.Profile,ProfileAdmin)