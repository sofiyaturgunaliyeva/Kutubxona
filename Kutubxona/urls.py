from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('bosh_s/', bosh_sahifa),
    path('mashq/', mashq_uchun),
    path('talaba/', talabalar),
    path('bitiruvchi/', bitiruvchilar),
    path('talaba/<int:son>/', bitta_talaba),
    path('yangi/', topshiriq),
    path('bitta_record/<int:son>/', bitta_record),
    path('mualliflar/', hamma_muallif),
    path('muallif/<int:son>/', bitta_muallif),
    path('kitob/<int:son>/',bitta_kitob),
    path('recordlar/',hamma_record),
    path('tirik/',tirik_mualliflar),
    path('muallif_kitob/',muallif_kitob),
    path('record/<int:son>/',record),
    path('record_bitiruvchi/',bitiruvchi),
    path('uchta/',uchta),
    path('uchta_m/',uchta_m),
    path('uchta_record/',uchta_record),
    path('kitoblari/',tirik),
    path('badiiy/', badiiy_kitoblar),
    path('talaba_ochir/<int:son>/',talaba_ochir ),
    path('uchta_muallif/',uchta_muallif ),
    path('kitob_ochir/<int:son>/',kitob_ochir ),
    path('vazifa1/',vazifa1),
    path('vazifa2/<int:son>/',vazifa2),
    path('vazifa3/<int:son>/',vazifa3),
    path('vazifa4/',vazifa4),
    path('hamma_kitoblar/',hamma_kitoblar),
    path('adminlar/',adminlar),
    path('talaba_edit/<int:son>/',talaba_ozgartir),
    path('kitob_ozgartir/<int:son>/',kitob_ozgartir),
    path('admin_ozgartir/<int:son>/',admin_ozgartir),
    path('muallif_ozgartir/<int:son>/',muallif_ozgartir),
    path('record_ozgartir/<int:son>/',record_ozgartir),
    path('',login_view, name = 'login'),
    path('logout/',logout_view),
    path('register/',register),

]
