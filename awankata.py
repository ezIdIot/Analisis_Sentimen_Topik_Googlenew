from multiprocessing.resource_sharer import stop
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import listkatastop as lks
import analisissentimen as ase
import numpy as np
import pandas as pd
from PIL import Image

def tampilkan_awan_kata(isi_text, topik):
    #print(isi_text)
    mask = np.array(Image.open('comment3.png'))
    stop_words = lks.list_kata_stop(topik)
    wordcloud = WordCloud(stopwords = stop_words, width=1600, height=800, max_font_size=200, background_color='white', mask=mask)
    wordcloud.generate(isi_text)
    plt.figure(figsize=(9,7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.suptitle(topik.capitalize(),fontsize=20)
    plt.show()

def tampilkan_sentimen(teks, topik):
    stop_words = lks.list_kata_stop(topik)
    teks_ntrl = ase.teks_netral(teks,topik)
    teks_pos = ase.teks_positif(teks,topik)
    teks_neg = ase.teks_negatif(teks,topik)

    df_netral = pd.DataFrame(teks_ntrl.split())
    df_positif = pd.DataFrame(teks_pos.split())
    df_negatif = pd.DataFrame(teks_neg.split())


    mask = np.array(Image.open('comment3.png'))
    word_cloud_lengkap = WordCloud(
        width=3000,
        height=2000,
        random_state=123,
        background_color="purple",
        colormap="Set2",
        collocations=False,
        stopwords=stop_words,
        mask=mask
    ).generate(teks)

    word_cloud_netral = WordCloud(
        width=3000,
        height=2000,
        random_state=123,
        background_color="purple",
        colormap="Set2",
        collocations=False,
        stopwords=stop_words,
        mask=mask
    ).generate(teks_ntrl)

    word_cloud_positif = WordCloud(
        width=3000,
        height=2000,
        random_state=123,
        background_color="purple",
        colormap="Set2",
        collocations=False,
        stopwords=stop_words,
        mask=mask
    ).generate(teks_pos)

    word_cloud_negatif = WordCloud(
        width=3000,
        height=2000,
        random_state=123,
        background_color="purple",
        colormap="Set2",
        collocations=False,
        stopwords=stop_words,
        mask=mask
    ).generate(teks_neg)


    rows=2
    cols=2
    fig, ax = plt.subplots(rows, cols, figsize=(12.5,6.5))
    ax[0][0].imshow(word_cloud_lengkap)
    ax[0][0].set_title("Lengkap")
    ax[0][0].axis("off")

    ax[0][1].imshow(word_cloud_netral)
    ax[0][1].set_title("Netral")
    ax[0][1].axis("off")

    ax[1][0].imshow(word_cloud_positif)
    ax[1][0].set_title("Positif")
    ax[1][0].axis("off")

    ax[1][1].imshow(word_cloud_negatif)
    ax[1][1].set_title("Negatif")
    ax[1][1].axis("off")

    plt.suptitle("Analisis Sentimen : "+topik.capitalize(),fontsize=20)
    plt.show()

    print()
    print("Kata-kata Netral yang ditemukan dalam Topik Berita :")
    print(df_netral.value_counts(sort=True))
    print()
    print("Kata-kata Positif yang ditemukan dalam Topik Berita :")
    print(df_positif.value_counts(sort=True))
    print()
    print("Kata-kata Negatif yang ditemukan dalam Topik Berita :")
    print(df_negatif.value_counts(sort=True))
