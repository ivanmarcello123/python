# matriks= [[5,1,3],
#           [2,6,7],
#           [9,4,8]]

# for i in range(3):
#     for j in range(3):
#         print(f"matriks [{i}]{[j]}={matriks}[{i}]{[j]}")


matriks = []
print("Masukkan 6 bilangan: ")

# looping untuk mengambil input dari user dan simpan ke dalam list
for i in range(3):
    # deklarasi sebuah list kosong untuk menyimpan setiap baris
    baris = []
    for j in range(3):
        bil = int(input(f"Input bilangan untuk baris {i+1}, kolom {j+1}: "))
        baris.append(bil)
    matriks.append(baris)

# Menampilkan matriks yang telah diinput
print("Bilangan dalam matriks adalah:")
for i in range(3):
    for j in range(3):
        print(f'matriks[{i+1}][{j+1}] = {matriks[i][j]}')
