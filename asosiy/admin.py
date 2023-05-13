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

# Vazifa 2  Muallifni ModelAdmin orqali qayta registratsiya qiling.
# Ismi bo’yicha qidirish, tirik-tirik emasligi bo’yicha filterlash imkoniyatlari bo’lsin.
# Id va ism ustunlarini linkka aylantiring.
# Kitob soni va tirikligi haqidagi ma’lumotni editable qiling.
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ("id","ism", "kitob_soni", "tirik")
    search_fields = ("ism",)
    search_help_text = "Kitob nomi va muallif ismi bo'yicha"
    list_filter = ("tirik",)
    list_display_links = ("id","ism")
    list_editable = ("kitob_soni","tirik")



# 1-topshiriq.  Admin modelini ModelAdmin orqali qayta registratsiya qiling.
# Adminni ish vaqti bo’yicha filterlash, ismi bo’yicha qidirish imkoniyatlari bo’lsin
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("id","ism")
    search_fields = ("ism",)
    search_help_text = "ismi bo'yicha"
    list_filter = ("ish_vaqti",)



# 3-topshiriq Recordni ModelAdmin orqali qayta registratsiya qiling.
# Ma’lumot qo’shishda hamma FK’larni ham qidirish imkoniyati bo’lsin.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "talaba","kitob","admin")
    list_display_links = ("id",)
    search_fields = ("talaba__ism","kitob__nom","admin__ism")
    search_help_text = "talabaning ismi,kitobning nomi,adminning ismi bo'yicha"
    autocomplete_fields = ("talaba","kitob","admin")





# admin.site.register(Talaba)

# admin.site.register(Muallif)

# admin.site.register(Kitob)

# admin.site.register(Admin)

# admin.site.register(Record)