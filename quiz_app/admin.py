from django.contrib import admin

# Register your models here.
from quiz_app.models import Question, Category, Level

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Level)
