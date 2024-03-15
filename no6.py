def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Konversi Suhu")
    print("Pilih konversi yang diinginkan:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")

    # Meminta input pilihan dari pengguna
    pilihan = int(input("Masukkan pilihan (1/2): "))

    if pilihan == 1:
        # Konversi dari Celsius ke Fahrenheit
        celsius = int(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("{} Celsius = {} Fahrenheit".format(celsius, fahrenheit))
    elif pilihan == 2:
        # Konversi dari Fahrenheit ke Celsius
        fahrenheit = int(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("{} Fahrenheit = {} Celsius".format(fahrenheit, celsius))
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
