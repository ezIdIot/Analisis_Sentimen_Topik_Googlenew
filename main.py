import nlpsource as nlp
import awankata as ak
import analisissentimen as ase

def print_list(list):
    i=1
    for item in list:
        print(i, item)
        i+=1


topik = input("Silahkan masukan topik berita : ")

list_judul= nlp.ambil_berita(topik)
if len(list_judul)>0:
    print_list(list_judul)
    teks =' '.join(list_judul)
    
    print()
    skor, hasil = ase.sentimen(teks,topik)
    print("Skor Analisis Sentimen :", skor)
    print("Sentimen topik berita",topik.capitalize(),"di Googlenews adalah",hasil)
    print()
    #ak.tampilkan_awan_kata(teks,topik)
    ak.tampilkan_sentimen(teks,topik)

else:
    print("Gagal ambil data dari Google News")
