import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

while True:
    liste = []
    n = int(input("Lütfen bir sayı giriniz: "))
    for i in range(1, n):
        deneme_sayisi = i + 1
        zar_atis = np.random.randint(1, 7, size=deneme_sayisi)  # Zar atışı
        herhangi_sayi_olasiligi = np.sum(zar_atis == 1) / deneme_sayisi  # Herhangi bir sayının gelme olasılığı
        liste.append(herhangi_sayi_olasiligi)
        print("Deneme Sayisi: {} -- Ortalama: {}".format(deneme_sayisi, herhangi_sayi_olasiligi))

    sns.lineplot(data=liste, linewidth=2)
    plt.xlabel("Deneme Sayisi")
    plt.ylabel("Ortalama")
    plt.ylim(0, 1)
    plt.axhline(1 / 6, linestyle="--", linewidth=1.5, color="red")  # Zarın herhangi bir sayısının beklenen olasılığı
    plt.show()
