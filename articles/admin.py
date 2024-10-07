from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_False = []
        is_True = []
        for form in self.forms:
            condition = form.cleaned_data.get('is_main')
            if condition == False:
                is_False.append(condition)
            elif condition == True:
                is_True.append(condition)
        if len(is_True) > len(is_False):
            raise ValidationError('Основным может быть только один раздел')
        elif len(is_True) == 0:
            raise ValidationError('Укажите основной раздел')
        elif len(is_False) == 0 and len(is_True) == 1:
            pass
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    ordering = ('-is_main',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]


@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['tag', 'article', 'is_main']


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']

