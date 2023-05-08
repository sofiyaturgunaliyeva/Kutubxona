from django.contrib import admin

from .models import *

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id","ism","kurs","kitob_soni")
    list_display_links = ("ism",)
    list_editable = ("kurs","kitob_soni")
    list_filter = ("kurs",)
    search_fields = ("ism","id","kitob_soni")
    search_help_text = "Ism, id, kitob_soni bo'yicha qidirish"
    # list_per_page = 5

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ("nom","janr","sahifa")
    list_display_links = ("nom",)
    list_editable = ("sahifa",)
    search_fields = ("nom","muallif__ism")
    search_help_text = "Kitob nomi va muallif ismi bo'yicha"
    list_filter = ("janr",)
    autocomplete_fields = ("muallif",)

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    search_fields = ("ism",)



# admin.site.register(Talaba)

# admin.site.register(Muallif)

# admin.site.register(Kitob)

admin.site.register(Admin)

admin.site.register(Record)