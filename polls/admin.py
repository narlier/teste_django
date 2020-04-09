from django.contrib import admin
from .models import Fornecedor, Resposta, Pergunta


class ChoiceInline(admin.TabularInline):
    model = Resposta
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["pergunta"]}),
        (
            "Datas de Publicação",
            {"fields": ["data_publicacao"], "classes": ["collapse"]},
        ),
    ]
    inlines = [ChoiceInline]
    list_display = ("pergunta", "data_publicacao")
    list_filter = ["data_publicacao"]
    search_fields = ["pergunta"]


admin.site.register(Fornecedor)
admin.site.register(Pergunta, QuestionAdmin)
