print("=======================================================================")
print("|                    PROGRAM INPUT NILAI MAHASISWA                    |")
print("=======================================================================")

nilai= []
perulangan = True

while perulangan:
    nama = input("Masukan Nama : ")
    nim = input("Masukan NIM : ")
    Tugas = int(input("Masukan Nilai Tugas : "))
    Uts = int(input("Masukan Nilai UTS : "))
    Uas = int(input("Masukan Nilai UAS : "))

    N1=Tugas*30/100
    N2=Uts*35/100
    N3=Uas*35/100

    nilai_Akhir=Tugas+Uas+Uts
    nilai.append([nama, nim, Tugas, Uts, Uts, Uas, int(nilai_Akhir)])
    if (input("Tambah data (y/t)? ") == 't'):
        break

print("\n                           DAFTAR NAILAI MAHASISWA                 ")
print("=====================================================================")
print("| No |    NAMA    |   NIM    |   TUGAS   |   UTS   |  UAS  |  AKHIR  |")
print("=====================================================================")
i = 0
for item in nilai:
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {nilaiTugas:5d} | {nilaiUTS:5d} | {nilaiUAS:5d} | {nilaiAKHIR:6.2F} |"
          .format(no=i, nama=item[0], nim=item[1], nilaiTugas=item[2], nilaiUTS=item[3], nilaiUAS=item[4], nilaiAKHIR=item[5]))
print("====================================================================")