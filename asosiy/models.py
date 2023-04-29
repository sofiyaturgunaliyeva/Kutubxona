from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    kitob_soni = models.SmallIntegerField()
    kurs = models.SmallIntegerField()

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    tanlov = [
        ("Erkak","Erkak"),
        ("Ayol","Ayol")
    ]
    ism = models.CharField(max_length=50)
    kitob_soni = models.SmallIntegerField()
    jins = models.CharField(max_length=50 , choices=tanlov)
    tirik = models.BooleanField()
    tugilgan_yili = models.SmallIntegerField()
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=50)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    sahifa= models.SmallIntegerField()
    janr = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Admin(models.Model):
    ish_vaqti_tanlov = [
        ("8:00 dan 12:00 gacha","8:00 dan 12:00 gacha"),
        ("12:00 dan 17:00 gacha","12:00 dan 17:00 gacha")
    ]

    Admin_ismi_tanlov = [
        ("Madina","Madina"),
        ("Malika","Malika")
    ]
    ism = models.CharField(max_length=50, choices=Admin_ismi_tanlov)
    ish_vaqti = models.CharField(max_length=50, choices=ish_vaqti_tanlov)
    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin= models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytargan_sana = models.DateField(null=True, blank=True)

