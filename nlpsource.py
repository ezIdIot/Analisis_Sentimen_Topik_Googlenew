from unittest import result
import urllib3
from collections import OrderedDict
from GoogleNews import GoogleNews 

http = urllib3.PoolManager()

urls_neg={}
urls_neg['negatif_1'] = 'https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/negative_keyword.txt'
urls_neg['negatif_2'] = 'https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/negatif_ta2.txt'
urls_neg['negatif_3'] = 'https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/negative_add.txt'
urls_neg['negatif_4'] = 'https://raw.githubusercontent.com/masdevid/ID-OpinionWords/master/negative.txt'
urls_neg['negatif_5'] = 'https://raw.githubusercontent.com/riochr17/Analisis-Sentimen-ID/master/data/negatif.txt'

urls_pos={}
urls_pos['positif_1'] = 'https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/positif_ta2.txt'
urls_pos['positif_2'] = 'https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/positive_add.txt'
urls_pos['positif_3'] = 'https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/positive_keyword.txt'
urls_pos['positif_4'] = 'https://raw.githubusercontent.com/masdevid/ID-OpinionWords/master/positive.txt'
urls_pos['positif_5'] = 'https://raw.githubusercontent.com/riochr17/Analisis-Sentimen-ID/master/data/positif.txt'

urls_stop={}
urls_stop['stop_1']='https://raw.githubusercontent.com/yasirutomo/python-sentianalysis-id/master/data/feature_list/stopwordsID.txt'
urls_stop['stop_2']='https://raw.githubusercontent.com/ramaprakoso/analisis-sentimen/master/kamus/stopword.txt'

def ambil_kata_negatif():
    kata_negatif =[]
    #Negatif 
    for url in urls_neg :
        #print(url)
        resp = http.request('GET', urls_neg[url])
        raw = resp.data.decode('utf-8')
        #print(raw)
        rawsplit = raw.lower().split()
        #print(rawsplit)
        kata_negatif.extend(rawsplit)

    #print(len(kata_negatif))
    #Hapus Duplicate
    result = list(OrderedDict.fromkeys(kata_negatif)) 
    #print(len(result))
    return result

def ambil_kata_positif():
    kata_positif =[]
    #Negatif 
    for url in urls_pos :
        #print(url)
        resp = http.request('GET', urls_pos[url])
        raw = resp.data.decode('utf-8')
        #print(raw)
        rawsplit = raw.lower().split()
        #print(rawsplit)
        kata_positif.extend(rawsplit)

    #print(len(kata_positif))
    #Hapus Duplicate
    result = list(OrderedDict.fromkeys(kata_positif)) 
    #print(len(result))
    return result

def ambil_kata_stoper():
    kata_stop =[]
    #Negatif 
    for url in urls_stop :
        #print(url)
        resp = http.request('GET', urls_stop[url])
        raw = resp.data.decode('utf-8')
        #print(raw)
        rawsplit = raw.lower().split()
        #print(rawsplit)
        kata_stop.extend(rawsplit)

    #print(len(kata_stop))
    #Hapus Duplicate
    result = list(OrderedDict.fromkeys(kata_stop)) 
    #print(len(result))
    return result

def ambil_berita(topik):
    googlenews = GoogleNews(lang='id',region="ID",encode='utf-8',period='1d')
    googlenews.get_news(topik.upper())
    result = googlenews.get_texts()
    googlenews.clear()
    return result