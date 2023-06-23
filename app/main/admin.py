from django.contrib import admin

from .models import PsychomatrixBaseContent, PsychomatrixAdditionalContent


@admin.register(PsychomatrixBaseContent)
class PsychomatrixBaseContentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PsychomatrixAdditionalContent)
class PsychomatrixAdditionalContentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
