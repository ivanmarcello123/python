# Memasukkan jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# List untuk menyimpan nilai siswa
nilai_siswa = []

# Memasukkan nilai untuk setiap siswa
for i in range(jumlah_siswa):
    print(f"\nMasukkan nilai untuk Siswa {i+1}:")
    aljabar = int(input("  Nilai Aljabar: "))
    geometri = int(input("  Nilai Geometri: "))
    kalkulus = int(input("  Nilai Kalkulus: "))
    statistika = int(input("  Nilai Statistika: "))
    nilai_siswa.append([aljabar, geometri, kalkulus, statistika])

# Menampilkan nilai kalkulus untuk semua siswa (kolom ke-3 / indeks 2)
nilai_kalkulus = [nilai[2] for nilai in nilai_siswa]
print(f"\nSemua nilai kalkulus: {nilai_kalkulus}")

# Menampilkan nilai kalkulus untuk siswa ke-2 (jika ada)


# Menampilkan semua nilai geometri (kolom ke-2)
nilai_geometri = [nilai[1] for nilai in nilai_siswa]
print(f"Semua nilai geometri: {nilai_geometri}")

# Menampilkan semua nilai aljabar (kolom ke-1)
nilai_aljabar = [nilai[0] for nilai in nilai_siswa]
print(f"Semua nilai aljabar: {nilai_aljabar}")

# Menampilkan semua nilai statistika (kolom ke-4)
nilai_statistika = [nilai[3] for nilai in nilai_siswa]
print(f"Semua nilai statistika: {nilai_statistika}")

# Menghitung rata-rata setiap siswa
rata_rata_siswa = []
for siswa in nilai_siswa:
    rata_rata_siswa.append(sum(siswa) / len(siswa))

print("\nRata-rata nilai setiap siswa:")
for i, rata in enumerate(rata_rata_siswa, start=1):
    print(f"Rata-rata siswa {i}: {rata:.2f}")

# Menghitung rata-rata untuk setiap mata pelajaran
rata_rata_mata_pelajaran = []
for j in range(len(nilai_siswa[0])):
    nilai_pelajaran = [nilai[j] for nilai in nilai_siswa]
    rata_rata_mata_pelajaran.append(sum(nilai_pelajaran) / len(nilai_pelajaran))

print("\nRata-rata nilai untuk setiap mata pelajaran:")
mata_pelajaran = ['Aljabar', 'Geometri', 'Kalkulus', 'Statistika']
for i, rata in enumerate(rata_rata_mata_pelajaran):
    print(f"Rata-rata nilai {mata_pelajaran[i]}: {rata:.2f}")
