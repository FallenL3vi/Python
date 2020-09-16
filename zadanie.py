import sqlite3
import re

def zmianaTypuZmiennej(tup):
    str = ''.join(tup)
    return str

slowa_funk = []
zaimki_lpoj = []
zaimki_lmn = []
zaimki = []

with open('slowa_funkcyjne.txt','r',encoding='utf-8') as file:
    for line in file:
        for word in re.findall(r'\w+',line):
            slowa_funk.append(word)

with open('zaimki.txt','r',encoding='utf-8') as file:
    for line in file:
        for word in re.findall(r'\w+',line):
            zaimki.append(word)

with open('zaimki_lpoj.txt','r',encoding='utf-8') as file:
    for line in file:
        for word in re.findall(r'\w+',line):
            zaimki_lpoj.append(word)

with open('zaimki_lmn.txt','r',encoding='utf-8') as file:
    for line in file:
        for word in re.findall(r'\w+',line):
            zaimki_lmn.append(word)

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("SELECT zawartosc FROM teksty")
zdania = []
numer = 1
wyniki = cursor.fetchall()
for r in wyniki:
    zdania.append(zmianaTypuZmiennej(r))
for w in zdania:
    liczba_f_s = 0
    liczba_zaimkow = 0
    liczba_zaimkow_p = 0
    liczba_zaimkow_m = 0
    #print(w)
    print("################################")
    print("*Tekst numer: " + str(numer) + "*")  
    print("Ilosc slow w tekscie: " + str(len(w.split())))
    print("Ilosc zdan w tekscie: " + str(len(re.findall(r'[.!?]+',w))))
    print("*****slowa_funkcyjne*****")
    for i in slowa_funk:
        print("{} ilosc wystapien: ".format(i) + str(len(re.findall(r'\b{}\b'.format(i),w))))
        liczba_f_s += len(re.findall(r'\b{}\b'.format(i),w))
    print("*****zaimki*****")
    for i in zaimki:
        print("{} ilosc wystapien: ".format(i) + str(len(re.findall(r'\b{}\b'.format(i),w))))
        liczba_zaimkow += len(re.findall(r'\b{}\b'.format(i),w))
    print("*****zaimki w 1 osobie l.poj*****")
    for i in zaimki_lpoj:
        print("{} ilosc wystapien: ".format(i) + str(len(re.findall(r'\b{}\b'.format(i),w))))
        liczba_zaimkow_p += len(re.findall(r'\b{}\b'.format(i),w))
    print("*****zaimki w 1 osobie l.mn*****")
    for i in zaimki_lmn:
        print("{} ilosc wystapien: ".format(i) + str(len(re.findall(r'\b{}\b'.format(i),w))))
        liczba_zaimkow_m += len(re.findall(r'\b{}\b'.format(i),w))
    numer += 1
    print("**********")
    print("Ilosc slow funkcyjnych w tekscie " + str(liczba_f_s))
    print("Ilosc zaimkow w tekscie: " + str(liczba_zaimkow))
    print("Ilosc zaimkow w liczbie mnogiej i 1 osobie: " + str(liczba_zaimkow_m))
    print("Ilosc zaimkow w liczbie pojedynczej i 1 osobie: " + str(liczba_zaimkow_p))
    print("################################")
cursor.close()
conn.close()
