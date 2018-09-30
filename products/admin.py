from django.contrib import admin

from .models import (
    Panels,
    PanelImage,
    Stabilizers,
    StabilizerImage,
    Ups,
    UpsImage,
    Genset,
    GensetDiesel,
    GensetDieselImage,
    GensetBenzine,
    GensetBenzineImage,
    GensetGas,
    GensetGasImage,
    GensetWelding,
    GensetWeldingImage,
    GensetAdditionalEquipment,
    GensetAdditionalImage
)


class PanelsImageInline(admin.TabularInline):
    model = PanelImage


class PanelsAdmin(admin.ModelAdmin):
    inlines = [
        PanelsImageInline
    ]


admin.site.register(Panels, PanelsAdmin)


class StabilizersImageInline(admin.TabularInline):
    model = StabilizerImage


class StabilizersAdmin(admin.ModelAdmin):
    inlines = [
        StabilizersImageInline
    ]


admin.site.register(Stabilizers, StabilizersAdmin)


class UpsImageInline(admin.TabularInline):
    model = UpsImage


class UpsAdmin(admin.ModelAdmin):
    inlines = [
        UpsImageInline
    ]


admin.site.register(Ups, UpsAdmin)

admin.site.register(Genset)


class GensetDieselImageInline(admin.TabularInline):
    model = GensetDieselImage


class GensetDieselAdmin(admin.ModelAdmin):
    inlines = [
        GensetDieselImageInline
    ]


admin.site.register(GensetDiesel, GensetDieselAdmin)


class GensetBenzineImageInline(admin.TabularInline):
    model = GensetBenzineImage


class GensetBenzineAdmin(admin.ModelAdmin):
    inlines = [
        GensetBenzineImageInline
    ]


admin.site.register(GensetBenzine, GensetBenzineAdmin)


class GensetGasImageInline(admin.TabularInline):
    model = GensetGasImage


class GensetGasAdmin(admin.ModelAdmin):
    inlines = [
        GensetGasImageInline
    ]


admin.site.register(GensetGas, GensetGasAdmin)


class GensetWeldingImageInline(admin.TabularInline):
    model = GensetWeldingImage


class GensetWeldingAdmin(admin.ModelAdmin):
    inlines = [
        GensetWeldingImageInline
    ]


admin.site.register(GensetWelding, GensetWeldingAdmin)


class GensetAdditionalImageInline(admin.TabularInline):
    model = GensetAdditionalImage


class GensetAdditionalAdmin(admin.ModelAdmin):
    inlines = [
        GensetAdditionalImageInline
    ]


admin.site.register(GensetAdditionalEquipment, GensetAdditionalAdmin)
