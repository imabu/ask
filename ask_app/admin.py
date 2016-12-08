from django.contrib import admin
from ask_app import models
from django.contrib import admin
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','author','rating',)


class AnswerAdmin(admin.ModelAdmin):
    list_display=('author','text','rating',)


class TagAdmin(admin.ModelAdmin):
    list_display=('value',)


class ProfileAdmin(admin.ModelAdmin):
    list_display=('nickname',)


class LikeQuestionAdmin(admin.ModelAdmin):
    list_display=('value',)


class LikeAnswerAdmin(admin.ModelAdmin):
    list_display=('value',)


admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.Answer,AnswerAdmin)
admin.site.register(models.Tag,TagAdmin)
admin.site.register(models.Profile,ProfileAdmin)
admin.site.register(models.LikeQuestion,LikeQuestionAdmin)
admin.site.register(models.LikeAnswer,LikeAnswerAdmin)
