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