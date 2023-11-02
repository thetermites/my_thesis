while True:
    liste = []
    n = int(input("Lütfen bir sayı giriniz"))
    for i in np.arange(1,n):
        deneme_sayisi = i + 1
        yazi_tura = np.random.randint(0,2,size = deneme_sayisi)
        yazi_olasiligi = np.mean(yazi_tura)
        liste.append (yazi_olasiligi)
        print("Deneme Sayisi: {}---------- OOrtalama {}".format(deneme_sayisi,yazi_olasiligi))
    
    
    sns.lineplot(data = liste,linewidth=2)
    plt.xlabel("Deneme Sayisi")
    plt.ylabel("Ortalama")
    plt.ylim(0,1)
    plt.axhline(0.5,linestyle = "--", linewidth = 1.5, color = "red")
    plt.show()
