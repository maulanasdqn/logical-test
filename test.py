# Pertemuan 2
# Aritmatika dan Pengkondisian Dasar

garis = "*"
namaPembuat = "Maulana"
greeting = "Selamat Datang Di Program Kalkulator " +  namaPembuat
menu = "1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian"

def penjumlahan(angka1, angka2):
    print (f"Hasil dari {angka1} Ditambah {angka2} Adalah {angka1 + angka2}")


print(garis * len(greeting))
print (greeting)
print(garis * len(greeting))
print(menu)
pilihan = int(input("Masukan Pilihan Anda : "))
angka1 = int(input("Masukkan Angka Pertama : "))
angka2 = int(input("Masukkan Angka Kedua : "))

if pilihan == 1:
    penjumlahan(angka1, angka2)

