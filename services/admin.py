from django.contrib import admin

from .models import (
    Services,
    SingleService,
    ServiceImage,
    Montages,
    SingleMontage,
    MontageImage,
    Installations,
    SingleInstallation,
    InstallationImage
)


class SingleServiceImageInline(admin.TabularInline):
    model = ServiceImage


class SingleServiceAdmin(admin.ModelAdmin):
    inlines = [
        SingleServiceImageInline
    ]


admin.site.register(Services)
admin.site.register(SingleService, SingleServiceAdmin)


class SingleInstallationImageInline(admin.TabularInline):
    model = InstallationImage


class SingleInstallationAdmin(admin.ModelAdmin):
    inlines = [
        SingleInstallationImageInline
    ]


admin.site.register(Installations)
admin.site.register(SingleInstallation, SingleInstallationAdmin)


class SingleMontageImageInline(admin.TabularInline):
    model = MontageImage


class SingleMontageAdmin(admin.ModelAdmin):
    inlines = [
        SingleMontageImageInline
    ]


admin.site.register(Montages)
admin.site.register(SingleMontage, SingleMontageAdmin)
