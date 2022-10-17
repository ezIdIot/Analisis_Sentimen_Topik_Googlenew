import listkatastop as lks
import listkatanegatif as lkn
import listkatapositif as lkp
import re

def teks_bersih(teks):
    s = re.sub(r'[^a-zA-Z0-9]', ' ', teks.lower())
    s = re.sub(' +', ' ', s)
    return s.strip()

def hapus_kata_kata(teks_sumber,teks_hapus):
    list_hapus = teks_hapus.lower().split()
    katalarangan = list_hapus
    big_regex = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, katalarangan))) #re.compile('|'.join(map(re.escape, katalarangan)))
    hasil = big_regex.sub("", teks_sumber.lower())
    return teks_bersih(hasil)

def hapus_kata_stop(teks,topik):
    katalarangan = lks.list_kata_stop(topik)
    big_regex = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, katalarangan)))
    hasil = big_regex.sub("", teks_bersih(teks))
    return teks_bersih(hasil)

def hapus_kata_negatif(teks):
    katalarangan = lkn.list_kata_negatif()
    big_regex = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, katalarangan)))
    hasil = big_regex.sub("", teks_bersih(teks))
    return teks_bersih(hasil)

def hapus_kata_positif(teks):
    katalarangan = lkp.list_kata_positif()
    big_regex = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, katalarangan)))
    hasil = big_regex.sub("", teks_bersih(teks))
    return teks_bersih(hasil)

def teks_netral(teks,topik):
    teks_tanpa_stop = hapus_kata_stop(teks,topik)
    teks_tanpa_negatif = hapus_kata_negatif(teks_tanpa_stop)
    teks_ntrl = hapus_kata_positif(teks_tanpa_negatif)
    return teks_bersih(teks_ntrl)

def teks_negatif(teks,topik):
    teks_tanpa_stop = hapus_kata_stop(teks,topik)
    teks_ntrl = teks_netral(teks_tanpa_stop,topik)
    teks_tanpa_netral = hapus_kata_kata(teks_tanpa_stop,teks_ntrl)
    teks_tanpa_positif = hapus_kata_positif(teks_tanpa_netral)
    return teks_bersih(teks_tanpa_positif)

def teks_positif(teks,topik):
    teks_tanpa_stop = hapus_kata_stop(teks,topik)
    teks_ntrl = teks_netral(teks_tanpa_stop,topik)
    teks_tanpa_netral = hapus_kata_kata(teks_tanpa_stop,teks_ntrl)
    teks_tanpa_negatif = hapus_kata_negatif(teks_tanpa_netral)
    return teks_bersih(teks_tanpa_negatif)

def skor_sentimen(teks,topik):
    teks_ntrl = teks_netral(teks,topik)
    teks_neg = teks_negatif(teks,topik)
    teks_pos = teks_positif(teks,topik)
    kata_positif = teks_pos.split()
    kata_negatif = teks_neg.split()
    kata_netral = teks_ntrl.split()
    jml_kata_positif = len(lkp.list_kata_positif())
    jml_kata_negatif = len(lkn.list_kata_negatif())
    jml_kata_netral = len(kata_netral)
    total_kata = jml_kata_negatif + jml_kata_netral+ jml_kata_positif
    rasio_positif = (total_kata-jml_kata_positif)/total_kata
    rasio_negatif = (total_kata- jml_kata_negatif)/total_kata
    rasio_netral = 0
    total_kata_teks = len(kata_positif)+len(kata_netral)+len(kata_negatif)
    skor_sentimen = ((rasio_positif*len(kata_positif))+(rasio_netral*len(kata_netral))-(rasio_negatif*len(kata_negatif)))/total_kata_teks
    return skor_sentimen

def sentimen(teks,topik):
    skor = skor_sentimen(teks,topik)
    hasil_sentimen =""
    if skor>0.01:
        hasil_sentimen = "POSITIF"    
    elif skor<-0.01 :
        hasil_sentimen = "NEGATIF"
    else :
        hasil_sentimen = "NETRAL"
    return skor,hasil_sentimen

def hitung_kata(kata, teks):
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(kata), teks))
    return count

