from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import *

def salomlash(sorov):
    return HttpResponse("<h1>Salom Dunyo!</h1>")

def bosh_sahifa(sorov):
    return render(sorov , 'home.html')

def mashq_uchun(sorov):
    content = {
        "kitoblar": ["Ufq","Qo'rqma","O'tkan kunlar","Odamiylik muki"],
        "ism" : "Sofiya"
    }
    return render(sorov , 'mashq.html',content)


def bitiruvchilar(sorov):
    content = {
        "student" : Talaba.objects.filter(kurs=4)
    }
    return render(sorov , "Bitiruvchi_talabalar.html",content)

def bitta_talaba(sorov,son):
    content = {
        "talaba": Talaba.objects.get(id = son)
    }
    return render(sorov, 'bitta_talaba.html',content)

def topshiriq(sorov):
    content = {
        "talaba": Talaba.objects.filter(ism__icontains = "a")

    }
    return render(sorov, 'talabalar.html' , content)

def bitta_record(sorov, son):
    content = {
        "student": Record.objects.get(id = son)
    }
    return render(sorov , 'bitta_talaba.html', content)

# Vazifa
# 1- tpshiriq Hamma mualliflarni chiqaruvchi html/view yozing.

def hamma_muallif(sorov):
    content = {
        "mualliflar": Muallif.objects.all()
    }
    return render(sorov, 'barcha_mualliflar.html',content)

# 2-topshiriq  Tanlangan bitta muallifning hamma ma’lumotlarini chiqaruvchi html/view yozing.

def bitta_muallif(sorov,son):
    content = {
        "muallif": Muallif.objects.get(id = son)
    }
    return render(sorov, 'bitta_muallif.html',content)

# 3-topshiriq Hamma kitoblarni chiqaring.

# def hamma_kitob(sorov):
#     content = {
#         "kitoblar": Kitob.objects.all()
#     }
#     return render(sorov, 'barcha_mualliflar.html',content)

# 4- topshiriq Tanlangan biron id’dagi kitobning hamma ma’lumotlarini chiqaring.

def bitta_kitob(sorov,son):
    content = {
        "kitob": Kitob.objects.filter(id = son).first()
    }
    return render(sorov, 'bitta_muallif.html',content)

# 5-topshiriq Hamma recordlarni chiqaring.

def hamma_record(sorov):
    content = {
        "recordlar": Record.objects.all()
    }
    return render(sorov, 'barcha_recordlar.html',content)

# 6-topshiriq Tirik mualliflarni chiqaring.

def tirik_mualliflar(sorov):
    content = {
        "tiriklar": Muallif.objects.filter(tirik = True)
    }
    return render(sorov,'tirik_mualliflar.html',content)

# 7-topshiriq  Sahifasi eng katta 3 ta kitobni chiqaring.

def uchta(sorov):
    content = {
        "kitoblar": Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(sorov,'barcha_recordlar.html',content)

# 8-topshiriq  Kitobi eng ko’p 3 ta muallifni chiqaring

def uchta_m(sorov):
    content = {
        "mualliflar": Muallif.objects.order_by('-kitob_soni')[:3]
    }
    return render(sorov,'barcha_recordlar.html',content)

# 9-topshiriq Recordlarni olingan sanasi bo’yicha eng oxirgi 3 tasini chiqaring.

def uchta_record(sorov):
    content = {
        "recordlar": Record.objects.order_by('-olingan_sana')[:3]
    }
    return render(sorov,'barcha_recordlar.html',content)

# 10-topshiriq Tirik mualliflarning kitoblarini chiqaring.

def tirik(sorov):
    content = {
        "kitoblari": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(sorov, 'barcha_recordlar.html', content)

# 11-topshiriq Hamma ‘badiiy’ kitoblarni chiqaring.

def badiiy_kitoblar(sorov):
    content = {
        "badiiy": Kitob.objects.filter(janr = 'badiiy')
    }
    return render(sorov, 'barcha_recordlar.html',content)

# 12-topshiriq Tug’ilgan yilidan kelib chiqib yoshi eng katta bo’lgan 3 ta muallifni chiqaruvchi view/html yozing.

def uchta_muallif(sorov):
    content = {
        "mualliflar": Muallif.objects.order_by('tugilgan_yili')[:3]
    }
    return render(sorov,'barcha_recordlar.html',content)

# 13-topshiriq Kitob soni 10 tadan kichik bo’lgan mualliflarning hamma kitoblarini chiqaruvchi view/html yozing.

def muallif_kitob(sorov):
    content = {
        "kitoblar": Kitob.objects.filter(muallif__kitob_soni__lt = 10)
    }
    return render(sorov,'mashq.html',content)

# 14-topshiriq Tanlangan biron id’dagi recorddagi hamma ma’lumotlarni chiqaruvchi html/view yozing.

def record(sorov,son):
    content = {
        "recordlar": Record.objects.filter(id=son)
    }
    return render(sorov, 'mashq.html',content)

# 15-topshiriq Bitiruvchi studentlarga tegishli hamma recordlarni chiqaruvchi html/view yozing.

def bitiruvchi(sorov):
    content = {
        "recordlar": Record.objects.filter(talaba__kurs = 4)
    }
    return render(sorov, 'barcha_recordlar.html',content)


# topshiriq  Url orqali son yuborib, viewda id’si shu songa tegishli studentni o’chirib yuborish

def talabalar(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "student": Talaba.objects.all()
        }
    else:
        content = {
            "student": Talaba.objects.filter(ism__contains = soz)
        }
    return render(sorov , 'talabalar.html', content)

def talaba_ochir(sorov,son):
    Talaba.objects.get(id = son).delete()
    return redirect('/talaba/')


def kitob_ochir(sorov,son):
    Kitob.objects.get(id = son).delete()
    return redirect('/kitoblar/')

# topshiriq Kitoblarni nomi bo’yicha qidirish imkoniyatini qo’shing

def hamma_kitob(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "kitoblar": Kitob.objects.all()
        }
    else:
        content = {
            "kitoblar": Kitob.objects.filter(nom__contains=soz)
        }

    return render(sorov, 'barcha_mualliflar.html',content)

# Vazifa

# 1-topshiriq Hamma recordlarni chiqaruvchi sahifaga student ismi bo’yicha recordlarni qidirish imkoniyatini qo’shing.

def vazifa1(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "recordlar": Record.objects.all()
        }
    else:
        content = {
            "recordlar": Record.objects.filter(talaba__ism__contains=soz)
        }
        return render(sorov, 'Vazifa_uchun.html',content)


# 2-topshiriq  Biron muallifni o’chirib yuborish uchun view yozing.

def vazifa2(sorov,son):
    Muallif.objects.get(id = son).delete()
    return redirect('/mualliflar/')

# 3-topshiriq Biron recordni o’chirib yuborish uchun view yozing.

def vazifa3(sorov,son):
    Record.objects.get(id = son).delete()
    return redirect('/recordlar/')

# 4-topshiriq Hamma mualliflarni chiqaruvchi sahifaga muallifni ismi bo’yicha
# qidirish imkoniyatini qo’shing.

def vazifa4(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "mualliflar": Muallif.objects.all()
        }
    else:
        content = {
            "mualliflar": Muallif.objects.filter(ism__contains=soz)
        }

    return render(sorov, 'barcha_mualliflar.html',content)

