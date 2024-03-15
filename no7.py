def determine_winner(pemain1, pemain2):
    # Mengecek hasil permainan dan menentukan pemenang
    if pemain1 == pemain2:
        return "Seri"
    elif (pemain1 == 'batu' and pemain2 == 'gunting') or (pemain1 == 'gunting' and pemain2 == 'kertas') or (pemain1 == 'kertas' and pemain2 == 'batu'):
        return "Pemain 1"
    else:
        return "Pemain 2"

def main():
    print("Permainan Batu-Gunting-Kertas")
    print("Pilihan: batu, gunting, kertas")

    # Input dari dua pemain
    pemain1 = input("Pemain 1, masukkan pilihan: ").lower()
    pemain2 = input("Pemain 2, masukkan pilihan: ").lower()

    # Memastikan input valid
    choices = ['batu', 'gunting', 'kertas']
    if pemain1 not in choices or pemain2 not in choices:
        print("Pilihan tidak valid. Pastikan Anda memasukkan batu, gunting, atau kertas.")
        return

    # Menentukan pemenang dan mencetak hasilnya
    pemenang = determine_winner(pemain1, pemain2)
    print("Pemenangnya adalah:", pemenang)

# Menjalankan permainan
if __name__ == "__main__":
    main()
