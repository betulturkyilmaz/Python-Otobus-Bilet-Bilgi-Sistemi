from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import shutil
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import smtplib
import time

ekran = Tk()
ekran.title("OTOBÜS BİLET BİLGİ SİSTEMİ")                                                                                                               
ekran.geometry("500x500")

veritab = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bilet"
)
mycursor = veritab.cursor(buffered=True)
sondeg = 0

x = StringVar()
z = StringVar()

resim2 = Image.open("dene2.png")
yukle2 = ImageTk.PhotoImage(resim2)
goruntu2 = Label(ekran, image=yukle2)
goruntu2.image = yukle2
goruntu2.place(x=0, y=0)


imaj1 = PhotoImage(file="bilet.png")
resim1 = imaj1.subsample(4, 4)

imaj2 = PhotoImage(file="kisi.png")
resim2 = imaj2.subsample(4, 4)

imaj3 = PhotoImage(file="otobus.png")
resim3 = imaj3.subsample(4, 4)

imaj4 = PhotoImage(file="cikis.png")
resim4 = imaj4.subsample(4, 4)

imaj5 = PhotoImage(file="iptal.png")
resim5 = imaj5.subsample(4, 4)




def biletsatis():
    ekran4 = Toplevel(ekran)
    ekran4.title("BİLET SATIŞ")
    ekran4.geometry("1000x1000")

    resim10 = Image.open("dene2.png")
    yukle10 = ImageTk.PhotoImage(resim10)
    goruntu10 = Label(ekran4, image=yukle10)
    goruntu10.image = yukle10
    goruntu10.place(x=0, y=0)


    

    bekle = Button(ekran4,text="Bilet Satış",image=resim1,compound=TOP, command=biletsatis)
    bekle.place(x=220, y=20, height=100, width=100)

    mbilgi = Button(ekran4,text="Yolcu Bilgileri",image=resim2, compound=TOP, command=yolcu_bilgileri)
    mbilgi.place(x=340, y=20, height=100, width=100)

    buton3 = Button(ekran4,text="Seferler", compound=TOP,image=resim3, command=seferler)
    buton3.place(x=460, y=20, height=100, width=100)

    bsil101 = Button(ekran4,text="Bilet Sil",image=resim5, compound=TOP, command=biletsil)
    bsil101.place(x=580, y=20, height=100, width=100)

    cikis101 = Button(ekran4,text="Çıkış",image=resim4, compound=TOP, command=quit)
    cikis101.place(x=700, y=20, height=100, width=100)

    liste=["ANKARA","ANTALYA","İZMİR","BURSA","RİZE"]
    liste2=["ANKARA","ANTALYA","İZMİR","BURSA","RİZE"]
    liste4=["150"]
    liste5=["200"]
    liste6=["100"]
    liste7=["120"]
    liste8=["160"]
    liste9=["130"]
    bos=[""]
    def calıstır(event):
      if kalkis.get()=="ANKARA":
        varis['values']=liste2
        print(liste2)
      if kalkis.get()=="ANTALYA":
        varis['values']=liste2
        print(liste2)
      if kalkis.get()=="İZMİR":
        varis['values']=liste2
        print(liste2)
      if kalkis.get()=="BURSA":
        varis['values']=liste2
        print(liste2)
      if kalkis.get()=="RİZE":
        varis['values']=liste2
        print(liste2)
    def calistir2(event):
      if varis.get()=="ANKARA" and kalkis.get()=="ANTALYA":
        son['values']=liste4
      if varis.get()=="ANKARA" and kalkis.get()=="İZMİR":
        son['values']=liste5
      if varis.get()=="ANKARA" and kalkis.get()=="BURSA":
        son['values']=liste6
      if varis.get()=="ANKARA" and kalkis.get()=="RİZE":
          
        son['values']=liste5
      if varis.get()=="ANTALYA" and kalkis.get()=="ANKARA":
        son['values']=liste4
      if varis.get()=="ANTALYA" and kalkis.get()=="İZMİR":
        son['values']=liste9
      if varis.get()=="ANTALYA" and kalkis.get()=="BURSA":
        son['values']=liste6
      if varis.get()=="ANTALYA" and kalkis.get()=="RİZE":
        son['values']=liste5

      if varis.get()=="İZMİR" and kalkis.get()=="ANKARA":
        son['values']=liste6
      if varis.get()=="İZMİR" and kalkis.get()=="ANTALYA":
        son['values']=liste9
      if varis.get()=="İZMİR" and kalkis.get()=="BURSA":
        son['values']=liste6
      if varis.get()=="İZMİR" and kalkis.get()=="RİZE":
        son['values']=liste8

        
      if varis.get()=="BURSA" and kalkis.get()=="ANKARA":
        son['values']=liste4
      if varis.get()=="BURSA" and kalkis.get()=="İZMİR":
        son['values']=liste6
      if varis.get()=="BURSA" and kalkis.get()=="ANTALYA":
        son['values']=liste6
      if varis.get()=="BURSA" and kalkis.get()=="RİZE":
        son['values']=liste5

      if varis.get()=="RİZE" and kalkis.get()=="ANKARA":
        son['values']=liste5
      if varis.get()=="RİZE" and kalkis.get()=="İZMİR":
        son['values']=liste8
      if varis.get()=="RİZE" and kalkis.get()=="BURSA":
        son['values']=liste5
      if varis.get()=="RİZE" and kalkis.get()=="ANTALYA":
        son['values']=liste6

    

    yolcu = Label(ekran4, text="YOLCU BİLGİLERİ")
    yolcu.place(x=230, y=150)
    yolcu.config(font=("Arial", 12, "bold"))


    ad = Label(ekran4, text="Ad")
    ad.place(x=100, y=200)
    ad.config(font=("Arial", 12, "bold"))

    giris1 = Entry(ekran4, width=30,font=("Arial", 12, "bold"),background="#509CCE")
    giris1.place(x=180, y=200)

    soyad = Label(ekran4, text="Soyad")
    soyad.place(x=100, y=250)
    soyad.config(font=("Arial", 12, "bold"))

    giris2 = Entry(ekran4, width=30,font=("Arial", 12, "bold"),background="#509CCE")
    giris2.place(x=180, y=250)

    tc = Label(ekran4, text="TC")
    tc.place(x=100, y=300)
    tc.config(font=("Arial", 12, "bold"))

    giris3 = Entry(ekran4, width=30,font=("Arial", 12, "bold"),background="#509CCE")
    giris3.place(x=180, y=300)

    Telefon = Label(ekran4, text="Telefon")
    Telefon.place(x=100, y=350)
    Telefon.config(font=("Arial", 12, "bold"))

    giris4 = Entry(ekran4, width=30,font=("Arial", 12, "bold"),background="#509CCE")
    giris4.place(x=180, y=350)

    cinsiyet = Label(ekran4, text="Cinsiyet")
    cinsiyet.place(x=100, y=400)
    cinsiyet.config(font=("Arial", 12, "bold"))

    rd1 = Radiobutton(ekran4, text="Erkek", value="x", variable=z)
    rd1.place(x=250, y=400)

    rd2 = Radiobutton(ekran4, text="Kadın", value="y", variable=z)
    rd2.place(x=320, y=400)

    mail = Label(ekran4, text="E-Mail")
    mail.place(x=100, y=450)
    mail.config(font=("Arial", 12, "bold"))

    giris5 = Entry(ekran4, width=30,font=("Arial", 12, "bold"),background="#509CCE")
    giris5.place(x=180, y=450)


    sefer = Label(ekran4, text="SEFER BİLGİLERİ")
    sefer.place(x=650, y=150)
    sefer.config(font=("Arial", 12, "bold"))


    kalkiss = Label(ekran4, text="Kalkış")
    kalkiss.place(x=550, y=200)
    kalkiss.config(font=("Arial", 12, "bold"))

    kalkis = Combobox(ekran4, width=27)
    kalkis['values']=liste
    kalkis.bind('<<ComboboxSelected>>', calıstır)
    kalkis.place(x=630, y=200)
    kalkis.config(font=("Arial", 12, "bold"))

    variss = Label(ekran4, text="Varış")
    variss.place(x=550, y=250)
    variss.config(font=("Arial", 12, "bold"))

    varis = Combobox(ekran4, width=27)
    varis['values'] =liste2
    varis.bind('<<ComboboxSelected>>', calistir2)
    varis.place(x=630, y=250)
    
    varis.config(font=("Arial", 12, "bold"))


    tarih = Label(ekran4, text="Tarih")
    tarih.place(x=550, y=300)
    tarih.config(font=("Arial", 12, "bold"))

    combo3 = Combobox(ekran4, width=7)
    combo3['values'] = (
        "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    combo3.place(x=630, y=300)
    combo3.current(0)
    combo3.config(font=("Arial", 12, "bold"))

    combo4 = Combobox(ekran4, width=7)
    combo4['values'] = (
        "", "Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylul", "Ekim", "Kasim",
        "Aralik")
    combo4.place(x=720, y=300)
    combo4.current(0)
    combo4.config(font=("Arial", 12, "bold"))

    combo5 = Combobox(ekran4, width=7)
    combo5['values'] = (
        "", "2020", "2021", "2022", "2023", "2024")
    combo5.place(x=810, y=300)
    combo5.current(0)
    combo5.config(font=("Arial", 12, "bold"))

    saat = Label(ekran4, text="Saat")
    saat.place(x=550, y=350)
    saat.config(font=("Arial", 12, "bold"))

    giris6 = Entry(ekran4, width=29,font=("Arial", 12, "bold"),background="#509CCE")
    giris6.place(x=630, y=350)

    koltuk = Label(ekran4, text="Koltuk Numarası")
    koltuk.place(x=550, y=400)
    koltuk.config(font=("Arial", 12, "bold"))

    combo6 = Combobox(ekran4, width=7)
    combo6['values'] = (
        "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    combo6.place(x=700, y=400)
    combo6.current(0)
    combo6.config(font=("Arial", 12, "bold"))


    ucret=Label(ekran4, text="Ücret")
    ucret.place(x=550, y=450)
    ucret.config(font=("Arial", 12, "bold"))


    son=Combobox(ekran4, width=7)
    son['values']=bos
    son.place(x=700, y=450)
    son.current(0)
    son.config(font=("Arial", 12, "bold"))

    sef=Label(ekran4, text="Sefer Numarası")
    sef.place(x=550, y=500)
    sef.config(font=("Arial", 12, "bold"))


    mycursor.execute("select sefer_no from seferler")
    result = mycursor.fetchall()
    combo402 = Combobox(ekran4, width=7,font=("Arial", 12, "bold"),background="#509CCE")
    seferr = [""]
    for seferno in result:
        seferr.append(seferno)
    combo402['values'] = seferr
    combo402.place(x=700, y=500)
    combo402.current(0)


    def veriekle():
        global sorgu201
        mycursor = veritab.cursor()

        if z.get() == "x":
            cins = "Erkek"
        if z.get() == "y":
            cins = "Kadın"

        sorgu201 = "INSERT INTO biletsatiss (adi,soyad,tc,telefon,mail,cinsiyet,kalkis,varis,tarih,saat,sefer,koltuk_no,ucret) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        deger = (giris1.get(),giris2.get(),giris3.get(),giris4.get(),giris5.get(),cins, kalkis.get(),varis.get(),combo3.get()+combo4.get()+combo5.get(),giris6.get(),combo402.get(),combo6.get(),son.get())
        mycursor.execute(sorgu201, deger)

        veritab.commit()

        print(mycursor.rowcount, "yolcu eklendi.")

    def temizle():
        giris1.delete(0,END)
        giris2.delete(0,END)
        giris3.delete(0,END)
        giris4.delete(0,END)
        giris5.delete(0,END)
        kalkis.delete(0,END)
        varis.delete(0,END)
        combo3.delete(0,END)
        combo4.delete(0,END)
        combo5.delete(0,END)
        giris6.delete(0,END)
        combo6.delete(0,END)
        son.delete(0,END)
        
    
    bsat = Button(ekran4, text="BİLET SAT", width=20, command=veriekle)
    bsat.place(x=700, y=600)

    temizle = Button(ekran4, text="SAYFAYI TEMİZLE", width=20, command=temizle)
    temizle.place(x=500, y=600)


    
def yolcu_bilgileri():
    ekran5 = Toplevel(ekran)
    ekran5.title("YOLCU BİLGİLERİ")
    ekran5.geometry("1200x1000")

    resim10 = Image.open("dene3.png")
    yukle10 = ImageTk.PhotoImage(resim10)
    goruntu10 = Label(ekran5, image=yukle10)
    goruntu10.image = yukle10
    goruntu10.place(x=0, y=0)



    bekle = Button(ekran5,text="Bilet Satış",image=resim1,compound=TOP, command=biletsatis)
    bekle.place(x=300, y=20, height=100, width=100)

    mbilgi = Button(ekran5,text="Yolcu Bilgileri",image=resim2, compound=TOP, command=yolcu_bilgileri)
    mbilgi.place(x=420, y=20, height=100, width=100)

    buton3 = Button(ekran5,text="Seferler", compound=TOP,image=resim3, command=seferler)
    buton3.place(x=540, y=20, height=100, width=100)

    bsil = Button(ekran5,text="Bilet Sil",image=resim5, compound=TOP, command=biletsil)
    bsil.place(x=660, y=20, height=100, width=100)

    cikis101 = Button(ekran5,text="Çıkış",image=resim4, compound=TOP, command=quit)
    cikis101.place(x=780, y=20, height=100, width=100)


    def bagla():
        global sonuclar
        global sorgu1
        mycursor = veritab.cursor()

        sorgu1 = "SELECT adi,soyad,tc,telefon,mail,cinsiyet,kalkis,varis,tarih,saat,koltuk_no FROM biletsatiss "

        mycursor.execute(sorgu1)

        sonuclar = mycursor.fetchall()

    bagla()

    tree1 = ttk.Treeview(ekran5)
    tree1.config(height=25)
    style = ttk.Style(ekran5)
    style.theme_use("clam")
    style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

    tree1["columns"] = ("Ad", "Soyad", "Tc Kimlik No","Telefon","Mail", "Cinsiyet", "Kalkis", "Varis","Tarih","Saat","Koltuk No",)
    tree1.column("Ad", width=100,anchor='sw')
    tree1.column("Soyad", width=100,anchor='sw')
    tree1.column("Tc Kimlik No", width=80,anchor='sw')
    tree1.column("Telefon", width=80,anchor='sw')
    tree1.column("Mail", width=175,anchor='sw')
    tree1.column("Cinsiyet", width=55,anchor='sw')
    tree1.column("Kalkis", width=80,anchor='sw')
    tree1.column("Varis", width=80,anchor='sw')
    tree1.column("Tarih", width=85,anchor='sw')
    tree1.column("Saat", width=80,anchor='sw')
    tree1.column("Koltuk No", width=80,anchor='sw')

    tree1.heading("Ad", text="Ad",anchor='sw')
    tree1.heading("Soyad", text="Soyad",anchor='sw')
    tree1.heading("Tc Kimlik No", text="Tc Kimlik No",anchor='sw')
    tree1.heading("Telefon", text="Telefon",anchor='sw')
    tree1.heading("Mail", text="Mail",anchor='sw')
    tree1.heading("Cinsiyet", text="Cinsiyet",anchor='sw')
    tree1.heading("Kalkis", text="Kalkis",anchor='sw')
    tree1.heading("Varis", text="Varis",anchor='sw')
    tree1.heading("Tarih", text="Tarih",anchor='sw')
    tree1.heading("Saat", text="Saat",anchor='sw')
    tree1.heading("Koltuk No", text="Koltuk No",anchor='sw')

    

    for satir in range(len(sonuclar)):
        for sutun in range(1):
            tree1.insert("", 0, values=(sonuclar[satir]))

    tree1.place(x=0, y=150)

    
    
def seferler():
    ekran6 = Toplevel(ekran)
    ekran6.title("SEFERLER")
    ekran6.geometry("1000x1000")

    resim10 = Image.open("dene2.png")
    yukle10 = ImageTk.PhotoImage(resim10)
    goruntu10 = Label(ekran6, image=yukle10)
    goruntu10.image = yukle10
    goruntu10.place(x=0, y=0)



    bekle = Button(ekran6,text="Bilet Satış",image=resim1,compound=TOP, command=biletsatis)
    bekle.place(x=220, y=20, height=100, width=100)

    mbilgi = Button(ekran6,text="Yolcu Bilgileri",image=resim2, compound=TOP, command=yolcu_bilgileri)
    mbilgi.place(x=340, y=20, height=100, width=100)

    buton3 = Button(ekran6,text="Seferler", compound=TOP,image=resim3, command=seferler)
    buton3.place(x=460, y=20, height=100, width=100)

    bsil = Button(ekran6,text="Bilet Sil",image=resim5, compound=TOP, command=biletsil)
    bsil.place(x=580, y=20, height=100, width=100)

    cikis101 = Button(ekran6,text="Çıkış",image=resim4, compound=TOP, command=quit)
    cikis101.place(x=700, y=20, height=100, width=100)

    def bagla2():
        global sonuclar2
        global sorgu2
        mycursor = veritab.cursor()

        sorgu2 = "SELECT sefer_no,baslangicsube,bitissube,saat,tarih,plaka FROM seferler "

        mycursor.execute(sorgu2)

        sonuclar2 = mycursor.fetchall()

    bagla2()

    tree1 = ttk.Treeview(ekran6)
    tree1.config(height=15)
    style = ttk.Style(ekran)
    style.theme_use("clam")
    style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

    tree1["columns"] = ("Sefer No", "Başlangıç Şube", "Bitiş Şube","Saat","Tarih", "Plaka")
    tree1.column("Sefer No", width=100,anchor='sw')
    tree1.column("Başlangıç Şube", width=100,anchor='sw')
    tree1.column("Bitiş Şube", width=80,anchor='sw')
    tree1.column("Saat", width=120,anchor='sw')
    tree1.column("Tarih", width=80,anchor='sw')
    tree1.column("Plaka", width=115,anchor='sw')
    
    tree1.heading("Sefer No", text="Sefer No",anchor='sw')
    tree1.heading("Başlangıç Şube", text="Başlangıç Şube",anchor='sw')
    tree1.heading("Bitiş Şube", text="Bitiş Şube",anchor='sw')
    tree1.heading("Saat", text="Saat",anchor='sw')
    tree1.heading("Tarih", text="Tarih",anchor='sw')
    tree1.heading("Plaka", text="Plaka",anchor='sw')
    

    

    for satir in range(len(sonuclar2)):
        for sutun in range(1):
            tree1.insert("", 0, values=(sonuclar2[satir]))

    tree1.place(x=110, y=160)


    sefer = Button(ekran6,text="Sefer Ekle", compound=TOP, command=seferr)
    sefer.place(x=810, y=510, height=50, width=100)

def seferr():
    ekran7 = Toplevel(ekran)
    ekran7.title("SEFER  EKLE")
    ekran7.geometry("1000x1000")

    resim10 = Image.open("dene2.png")
    yukle10 = ImageTk.PhotoImage(resim10)
    goruntu10 = Label(ekran7, image=yukle10)
    goruntu10.image = yukle10
    goruntu10.place(x=0, y=0)



    sefer = Label(ekran7, text="Sefer Bilgilerini Giriniz")
    sefer.place(x=450, y=100)
    sefer.config(font=("Arial", 12, "bold"))


    ad1 = Label(ekran7, text="Sefer Numarası")
    ad1.place(x=270, y=150)
    ad1.config(font=("Arial", 12, "bold"))

    giris11 = Entry(ekran7, width=29,font=("Arial", 12, "bold"),background="#509CCE")
    giris11.place(x=420, y=150)


    ad2 = Label(ekran7, text="Başlangıç Şube")
    ad2.place(x=270, y=200)
    ad2.config(font=("Arial", 12, "bold"))


    combo1 = Combobox(ekran7, width=10)
    combo1['values'] = ("", "Ankara", "Antalya", "İzmir", "Bursa", "Rize")
    combo1.place(x=420, y=200)
    combo1.current(0)
    combo1.config(font=("Arial", 12, "bold"))


    ad3 = Label(ekran7, text="Bitiş Şube")
    ad3.place(x=270, y=250)
    ad3.config(font=("Arial", 12, "bold"))


    combo2 = Combobox(ekran7, width=10)
    combo2['values'] = ("", "Ankara", "Antalya", "İzmir", "Bursa", "Rize")
    combo2.place(x=420, y=250)
    combo2.current(0)
    combo2.config(font=("Arial", 12, "bold"))

    ad4 = Label(ekran7, text="Saat")
    ad4.place(x=270, y=300)
    ad4.config(font=("Arial", 12, "bold"))

    giris12 = Entry(ekran7, width=29,font=("Arial", 12, "bold"),background="#509CCE")
    giris12.place(x=420, y=300)


    tarih = Label(ekran7, text="Tarih")
    tarih.place(x=270, y=350)
    tarih.config(font=("Arial", 12, "bold"))

    combo3 = Combobox(ekran7, width=7)
    combo3['values'] = (
        "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    combo3.place(x=420, y=350)
    combo3.current(0)
    combo3.config(font=("Arial", 12, "bold"))

    combo4 = Combobox(ekran7, width=7)
    combo4['values'] = (
        "", "Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylul", "Ekim", "Kasim",
        "Aralik")
    combo4.place(x=510, y=350)
    combo4.current(0)
    combo4.config(font=("Arial", 12, "bold"))

    combo5 = Combobox(ekran7, width=7)
    combo5['values'] = (
        "", "2020", "2021", "2022", "2023", "2024")
    combo5.place(x=600, y=350)
    combo5.current(0)
    combo5.config(font=("Arial", 12, "bold"))

    ad5 = Label(ekran7, text="Plaka")
    ad5.place(x=270, y=400)
    ad5.config(font=("Arial", 12, "bold"))

    giris13 = Entry(ekran7, width=29,font=("Arial", 12, "bold"),background="#509CCE")
    giris13.place(x=420, y=400)

    def veriekle2():
        global sorgu202
        mycursor = veritab.cursor()


        sorgu202 = "INSERT INTO seferler (sefer_no,baslangicsube,bitissube,saat,tarih,plaka) VALUES (%s,%s,%s,%s,%s,%s)"
        deger2 = (giris11.get(),combo1.get(),combo2.get(),giris12.get(),combo3.get()+combo4.get()+combo5.get(),giris13.get())
        mycursor.execute(sorgu202, deger2)

        veritab.commit()

        print(mycursor.rowcount, " eklendi.")


    eklee = Button(ekran7, text="EKLE", width=20, command=veriekle2)
    eklee.place(x=700, y=500)

    
    
def biletsil():
    ekran8 = Toplevel(ekran)
    ekran8.title("BİLET SİL")
    ekran8.geometry("1200x1000")
    resim10 = Image.open("dene3.png")
    yukle10 = ImageTk.PhotoImage(resim10)
    goruntu10 = Label(ekran8, image=yukle10)
    goruntu10.image = yukle10
    goruntu10.place(x=0, y=0)


    
    bekle = Button(ekran8,text="Bilet Satış",image=resim1,compound=TOP, command=biletsatis)
    bekle.place(x=300, y=20, height=100, width=100)

    mbilgi = Button(ekran8,text="Yolcu Bilgileri",image=resim2, compound=TOP, command=yolcu_bilgileri)
    mbilgi.place(x=420, y=20, height=100, width=100)

    buton3 = Button(ekran8,text="Seferler", compound=TOP,image=resim3, command=seferler)
    buton3.place(x=540, y=20, height=100, width=100)

    bsil = Button(ekran8,text="Bilet Sil",image=resim5, compound=TOP, command=biletsil)
    bsil.place(x=660, y=20, height=100, width=100)

    cikis101 = Button(ekran8,text="Çıkış",image=resim4, compound=TOP, command=quit)
    cikis101.place(x=780, y=20, height=100, width=100)

    

    def goster1():
        global sonuclar
        global sorgu1
        mycursor = veritab.cursor()

        sorgu1 = "SELECT adi,soyad,tc,telefon,mail,cinsiyet,kalkis,varis,tarih,saat,koltuk_no FROM biletsatiss "

        mycursor.execute(sorgu1)

        sonuclar = mycursor.fetchall()

    goster1()

    tree1 = ttk.Treeview(ekran8)
    tree1.config(height=15)
    style = ttk.Style(ekran)
    style.theme_use("clam")
    style.configure("Treeview", background="white",fieldbackground="white", foreground="black")

    tree1["columns"] = ("Ad", "Soyad", "Tc Kimlik No","Telefon","Mail", "Cinsiyet", "Kalkis", "Varis","Tarih","Saat","Koltuk No",)
    tree1.column("Ad", width=100,anchor='sw')
    tree1.column("Soyad", width=100,anchor='sw')
    tree1.column("Tc Kimlik No", width=80,anchor='sw')
    tree1.column("Telefon", width=120,anchor='sw')
    tree1.column("Mail", width=80,anchor='sw')
    tree1.column("Cinsiyet", width=115,anchor='sw')
    tree1.column("Kalkis", width=80,anchor='sw')
    tree1.column("Varis", width=80,anchor='sw')
    tree1.column("Tarih", width=80,anchor='sw')
    tree1.column("Saat", width=80,anchor='sw')
    tree1.column("Koltuk No", width=80,anchor='sw')

    tree1.heading("Ad", text="Ad",anchor='sw')
    tree1.heading("Soyad", text="Soyad",anchor='sw')
    tree1.heading("Tc Kimlik No", text="Tc Kimlik No",anchor='sw')
    tree1.heading("Telefon", text="Telefon",anchor='sw')
    tree1.heading("Mail", text="Mail",anchor='sw')
    tree1.heading("Cinsiyet", text="Cinsiyet",anchor='sw')
    tree1.heading("Kalkis", text="Kalkis",anchor='sw')
    tree1.heading("Varis", text="Varis",anchor='sw')
    tree1.heading("Tarih", text="Tarih",anchor='sw')
    tree1.heading("Saat", text="Saat",anchor='sw')
    tree1.heading("Koltuk No", text="Koltuk No",anchor='sw')

    

    for satir in range(len(sonuclar)):
        for sutun in range(1):
            tree1.insert( "",0, values=(sonuclar[satir]))

    tree1.place(x=0, y=250)
    mycursor.execute("select tc from biletsatiss")
    result = mycursor.fetchall()
    combo401 = Combobox(ekran8, width=25,font=("Arial", 12, "bold"),background="#509CCE")
    tc = ["Tc Kimlik Numarasını Seçiniz"]
    for tcno in result:
        tc.append(tcno)
    combo401['values'] = tc
    combo401.place(x=400, y=160)
    combo401.current(0)




    def sill():
        global sorgu1
        mycursor = veritab.cursor()
        sorgu1 = "delete from biletsatiss where tc='"+ combo401.get() +"'"
        mycursor.execute(sorgu1)
        veritab.commit()
        print("silindi")

    buton404 = Button(ekran8, text=" Sil", command=sill)
    buton404.place(x=670, y=160)

ad = Label(text="Kullanıcı Adı")
ad.place(x=50, y=150)
ad.config(font=("Arial", 12, "bold"))


giris1 = Entry( width=30,font=("Arial", 12, "bold"),background="#509CCE")
giris1.place(x=180, y=150)


sifreee = Label( text="Şifre")
sifreee.place(x=50, y=200)
sifreee.config(font=("Arial", 12, "bold"))


giris2 = Entry( width=30,font=("Arial", 12, "bold"),background="#509CCE")
giris2.place(x=180, y=200)

imaj202 = PhotoImage(file="bilet.png")
resim202 = imaj202.subsample(3, 2)

imaj203 = PhotoImage(file="kisi.png")
resim203 = imaj203.subsample(3, 2)

imaj206 = PhotoImage(file="iptal.png")
resim206 = imaj206.subsample(4, 3)

imaj204 = PhotoImage(file="otobus.png")
resim204 = imaj204.subsample(3, 2)

imaj205 = PhotoImage(file="cikis.png")
resim205 = imaj205.subsample(4, 3)
def login():
    global sonuclar
    try:
        veritab = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bilet"
    )
    except:
        print("başarısız(localhost)")
    else:
        print("başarılı")

        
        mycursor = veritab.cursor()
        sql="select kadi,sifre from calisan_giris " 
        mycursor.execute(sql)
        for(kadi,sifre) in mycursor:
            if giris1.get()==kadi and giris2.get()==sifre:
                
                    ekran10 = Toplevel(ekran)
                    ekran10.title("ANASAYFA")
                    ekran10.geometry("1000x1000")
                    resim2 = Image.open("dene2.png")
                    yukle2 = ImageTk.PhotoImage(resim2)
                    goruntu2 = Label(ekran10, image=yukle2)
                    goruntu2.image = yukle2
                    goruntu2.place(x=0, y=0)

                    
                    

                    bekle = Button(ekran10,text="Bilet Satış",image=resim202,compound=TOP, command=biletsatis)
                    bekle.place(x=320, y=70, height=150, width=150)

                    

                    mbilgi = Button(ekran10,text="Yolcu Bilgileri",image=resim203, compound=TOP, command=yolcu_bilgileri)
                    mbilgi.place(x=520, y=70, height=150, width=150)

                    

                    buton3 = Button(ekran10,text="Seferler",image=resim204, compound=TOP, command=seferler)
                    buton3.place(x=320, y=250, height=150, width=150)

                    

                    bsil = Button(ekran10,text="Bilet Sil",image=resim206, compound=TOP, command=biletsil)
                    bsil.place(x=520, y=250, height=150, width=150)

                    

                    cikis101 = Button(ekran10,text="Çıkış",image=resim205,compound=TOP, command=quit)
                    cikis101.place(x=420, y=450, height=150, width=150)


            else:
                print("yanlış")

                            

            mycursor.close()
            veritab.close()
                            


    
    

   

gir = Button( text="GİRİŞ", width=20, command=login)
gir.place(x=230, y=250)

    



