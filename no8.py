def hitung_ipk(nilai_matkul):
    total_sks = 0
    total_nilai = 0

    for matkul, sks, nilai in nilai_matkul:
        total_sks += sks
        total_nilai += sks * nilai

    ipk = total_nilai / total_sks
    return ipk

def main():
    print("=== Perhitungan IPK ===")
    print("Masukkan nilai mata kuliah untuk semester ini:")
    print("Mata kuliah: Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan English 1")

    # List mata kuliah beserta SKS dan nilai
    mata_kuliah = ["Algoritma", "Perancangan Objek", "Kalkulus", "Etika Profesi", "Databases", "English 1"]
    sks_matkul = [3, 3, 4, 2, 3, 3]
    nilai_matkul = []

    # Meminta input nilai untuk setiap mata kuliah
    for i in range(len(mata_kuliah)):
        nilai = float(input("Masukkan nilai untuk {}: ".format(mata_kuliah[i])))
        nilai_matkul.append((mata_kuliah[i], sks_matkul[i], nilai))

    # Menghitung IPK
    ipk = hitung_ipk(nilai_matkul)

    print("IPK semester ini adalah:", ipk)

# Menjalankan program utama
if __name__ == "__main__":
    main()
