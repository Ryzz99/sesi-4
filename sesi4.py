# Masukan dua bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Membandingkan dua bilangan dan menampilkan hasilnya
if bilangan1 > bilangan2:
    print("Bilangan pertama ({}) lebih besar dari bilangan kedua ({})".format(bilangan1, bilangan2))
elif bilangan2 > bilangan1:
    print("Bilangan kedua ({}) lebih besar dari bilangan pertama ({})".format(bilangan2, bilangan1))
else:
    print("Kedua bilangan ({}) sama besar".format(bilangan1))
