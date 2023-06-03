from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

def salomlash(sorov):
    return HttpResponse("<h1>Salom Dunyo!</h1>")

def bosh_sahifa(sorov):
    return render(sorov , 'home.html')


def login_view(sorov):
    if sorov.method == "POST":
       user = authenticate(               # bor bo'lsa userni , yo'q bo'lsa None
            username = sorov.POST.get('l'),
            password = sorov .POST.get('p')
        )
       if user is None:
            return redirect("/")
       login(sorov,user)
       return redirect("/bosh_s/")
    return render(sorov, 'login.html')


def logout_view(sorov):
    logout(sorov)
    return redirect("/")


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
    if sorov.method == 'POST':
        f = MuallifForm(sorov.POST)
        if f.is_valid():
            Muallif.objects.create(
                ism=f.cleaned_data['ism'],
                kitob_soni=f.cleaned_data['k_s'],
                jins=f.cleaned_data['jinsi'],
                tirik=f.cleaned_data['tirik'],
                tugilgan_yili=f.cleaned_data['tugilgan_yili'],

        )
        return redirect('/mualliflar/')


    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "mualliflar": Muallif.objects.all(),
            "forma": MuallifForm()
        }
    else:
        content = {
            "mualliflar": Muallif.objects.filter(ism__contains=soz),
            "forma": MuallifForm()
        }

    return render(sorov, 'barcha_mualliflar.html', content)


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
    if sorov.user.is_authenticated:
        if sorov.method == 'POST':
            forma = RecordForm(sorov.POST)
            if forma.is_valid():
                forma.save()
            # Record.objects.create(
            #    talaba = Talaba.objects.get(id = sorov.POST.get('t')),
            #    kitob = Kitob.objects.get(id=sorov.POST.get('k')),
            #    admin = Admin.objects.get(id=sorov.POST.get('ad'))

            return redirect('/recordlar/')

        soz = sorov.GET.get('qidiruv')
        if soz == "" or soz is None:
            content = {
                "recordlar": Record.objects.all(),
                "student": Talaba.objects.all(),
                "kitoblar" : Kitob.objects.all(),
                "adminlar": Admin.objects.all(),
                "forma": RecordForm()
            }
        else:
            content = {
                # "recordlar": Record.objects.filter(talaba__ism__contains=soz)
                "student": Talaba.objects.filter(ism__contains=soz),
                "kitoblar": Kitob.objects.filter(nom__contains=soz),
                "adminlar": Admin.objects.filter(ism__contains=soz),
                "forma": RecordForm()
            }
        return render(sorov, 'barcha_recordlar.html', content)
    return redirect('/')


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
    if sorov.method == 'POST':
        f = TalabaForm(sorov.POST)
        if f.is_valid():
            Talaba.objects.create(
                ism = f.cleaned_data['ism'],
                kurs = f.cleaned_data.get('kursi'),
                kitob_soni = f.cleaned_data.get('k_s')

            )
        return redirect('/talaba/')

    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "student": Talaba.objects.all(),
            "forma": TalabaForm()

        }
    else:
        content = {
            "student": Talaba.objects.filter(ism__contains = soz),
            "talaba": TalabaForm()
        }
    return render(sorov , 'talabalar.html', content)

def talaba_ochir(sorov,son):
    Talaba.objects.get(id = son).delete()
    return redirect('/talaba/')


def kitob_ochir(sorov,son):
    Kitob.objects.get(id = son).delete()
    return redirect('/hamma_kitoblar/')

# topshiriq Kitoblarni nomi bo’yicha qidirish imkoniyatini qo’shing

def hamma_kitoblar(sorov):
    if sorov.method == 'POST':
        forma = KitobForm(sorov.POST)
        if forma.is_valid():
            forma.save()
        # Kitob.objects.create(
        #    nom = sorov.POST.get('nomi'),
        #    sahifa = sorov.POST.get('s'),
        #    janr = sorov.POST.get('j'),
        #    muallif = Muallif.objects.get(id = sorov.POST.get('m'))
        # )
        return redirect('/hamma_kitoblar/')


    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "kitoblar": Kitob.objects.all(),
            "mualliflar": Muallif.objects.all(),
            "forma":KitobForm()
        }
    else:
        content = {
            "kitoblar": Kitob.objects.filter(nom__contains=soz),
            "mualliflar": Muallif.objects.filter(ism__contains=soz),
            "forma" : KitobForm()
        }

    return render(sorov, 'Kitoblar.html',content)


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

# Vazifa

def adminlar(sorov):
    if sorov.method == 'POST':
        f = AdminForm(sorov.POST)
        if f.is_valid():
            Admin.objects.create(
               ism = f.cleaned_data['ismi'],
               ish_vaqti = f.cleaned_data['ish_vaqti']
            )
        return redirect('/adminlar/')
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "adminlar": Admin.objects.all(),
            "forma": AdminForm()
        }
    else:
        content = {
            "adminlar": Admin.objects.filter(ism__contains=soz),
            "forma": AdminForm()
        }
    return render(sorov, 'Adminlar.html',content)

def talaba_ozgartir(sorov,son):
    if sorov.method == 'POST':
        Talaba.objects.filter(id = son).update(
            ism = sorov.POST.get('i'),
            kitob_soni = sorov.POST.get('k_s'),
            kurs = sorov.POST.get('k')
        )
        return redirect('/talaba/')
    content={
        "talaba":Talaba.objects.get(id = son)
    }
    return render(sorov,'talaba_ozgartir.html',content)

def kitob_ozgartir(sorov,son):
    if sorov.method == 'POST':
        Kitob.objects.filter(id = son).update(
            nom= sorov.POST.get('n'),
            sahifa = sorov.POST.get('s'),
            janr = sorov.POST.get('j'),
            muallif = Muallif.objects.get(id = sorov.POST.get('m'))
        )
        return redirect('/hamma_kitoblar/')
    k = Kitob.objects.get(id = son)
    content={
        "kitob":k,
        "mualliflar" : Muallif.objects.exclude(id = k.muallif.id)
    }
    return render(sorov,'kitob_ozgartir.html',content)

# Vazifa
# 1-topshiriq  Tanlangan admin ma’lumotini tahrir qilish imkoniyatini qo’shing.

def admin_ozgartir(sorov,son):
    if sorov.method == 'POST':
        Admin.objects.filter(id = son).update(
            ism= sorov.POST.get('i'),
            ish_vaqti = sorov.POST.get('i_v')
        )
        return redirect('/adminlar/')
    content={
        "admin" : Admin.objects.get(id = son)
    }
    return render(sorov,'admin_ozgartir.html',content)

# 2-topshiriq Tanlangan muallif ma’lumotini tahrir qilish imkoniyatini qo’shing.

def muallif_ozgartir(sorov,son):
    if sorov.method == 'POST':
        Muallif.objects.filter(id = son).update(
            ism= sorov.POST.get('i'),
            kitob_soni = sorov.POST.get('k_s'),
            jins = sorov.POST.get('j'),
            tirik = True,
            tugilgan_yili = sorov.POST.get('t_y')

        )
        return redirect('/mualliflar/')
    content={
        "muallif" : Muallif.objects.get(id = son)
    }
    return render(sorov,'muallif_ozgartir.html',content)


# 3-topshiriq  Record ma’lumotlari uchun o’zgartirish imkoniyati qo’shing.
# Faqat qaytardi va qaytarish sanasi ma’lumotlarini o’zgartirish imkoniyati bo’lsin xolos.

def record_ozgartir(sorov, son):
    if sorov.method == 'POST':
        Record.objects.filter(id=son).update(
            talaba=Talaba.objects.get(id=sorov.POST.get('t')),
            kitob=Kitob.objects.get(id=sorov.POST.get('k')),
            admin=Admin.objects.get(id=sorov.POST.get('ad')),
            qaytargan_sana=sorov.POST.get('q')
        )
        return redirect('/recordlar/')

    content = {
        "record": Record.objects.get(id=son),
        "talabalar": Talaba.objects.all(),
        "kitoblar": Kitob.objects.all(),
        "adminlar": Admin.objects.all()
    }
    return render(sorov, 'record_ozgartir.html', content)


def register(sorov):
    if sorov.method == 'POST' and sorov.POST.get('p') == sorov.POST.get('p2'):
        User.objects.create_user(
            username = sorov.POST.get('l'),
            password = sorov.POST.get('p')
        )
        return redirect('login')
    return render(sorov,'register.html')