# Masukan input untuk sebuah bilangan
bilangan = int(input("Masukkan sebuah bilangan: "))

# Menentukan apakah bilangan tersebut positif, negatif, atau nol
if bilangan > 0:
    print("Bilangan", bilangan, "adalah bilangan positif")
elif bilangan < 0:
    print("Bilangan", bilangan, "adalah bilangan negatif")
else:
    print("Bilangan", bilangan, "adalah nol")

# Menentukan apakah bilangan tersebut ganjil atau genap
if bilangan % 2 == 0:
    print("Bilangan", bilangan, "adalah bilangan genap")
else:
    print("Bilangan", bilangan, "adalah bilangan ganjil")
