from .models import *
from django import forms

# 1-si forms.Form , 2-si

class TalabaForm(forms.Form):
    def validate_ism(qiymat):
        if len(qiymat) < 3:
            raise Exception("Bunday ism  bo'lmaydi")
        return qiymat
    ism = forms.CharField(validators=[validate_ism])
    kursi = forms.IntegerField(min_value=1, max_value=4)
    k_s = forms.IntegerField(label = "Kitoblari soni")

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'   # hammasini oladi

# Vazifa
# 1-topshiriq Muallif qo’shishni django form orqali qayta bajaring.

class MuallifForm(forms.Form):
    TANLOV = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    ]

    ism = forms.CharField()
    k_s = forms.IntegerField(label="Kitoblari soni")
    jinsi = forms.ChoiceField(choices=TANLOV)
    tirik = forms.BooleanField()
    tugilgan_yili = forms.IntegerField()

# 2-topshiriq  Record qo’shishni djangodagi ModelFormdan foydalanib qayta bajaring.

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

# 3-topshiriq   Admin qo’shishni django form orqali qayta bajaring.
class AdminForm(forms.Form):
    ish_vaqti_tanlov = [
        ("8:00 dan 12:00 gacha", "8:00 dan 12:00 gacha"),
        ("12:00 dan 17:00 gacha", "12:00 dan 17:00 gacha")
    ]

    Admin_ismi_tanlov = [
        ("Madina", "Madina"),
        ("Malika", "Malika")
    ]
    ismi = forms.ChoiceField(choices=Admin_ismi_tanlov)
    ish_vaqti = forms.ChoiceField(choices=ish_vaqti_tanlov)
