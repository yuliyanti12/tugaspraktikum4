# tugaspraktikum4
Program Menghitung Nilai Mahasiswa
Praktek kali ini, saya akan membuat program menghitung menentukan nilai mahasiswa dengan menggunakan list.

Contoh Code dan Penjelasan
print("==================================================================")

print("| PROGRAM INPUT DATA NILAI MAHASISWA |") print("==================================================================")

nilai = [] perulangan = True

while perulangan: nama = input("Masukan Nama: ") nim = input("Masukan NIM: ") nilaiTugas = int(input("Masukan nilai Tugas: ")) nilaiUts = int(input("Masukan nilai UTS: ")) nilaiUas = int(input("Masukan nilai UAS: ")) nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUts * 35/100) + (nilaiUas * 35/100)

nilai.append([nama, nim, nilaiTugas, nilaiUts, nilaiUas, int(nilaiAkhir)])
if (input("Tambah data (y/t)? ") == 't'):
    perulangan = False
print("\n DAFTAR NILAI MAHASISWA ") print("==================================================================") print("| No | Nama | NIM | Tugas | UTS | UAS | Akhir |") print("==================================================================")

i = 0 for item in nilai: i += 1 print("| {no:2d} | {nama:12s} | {nim:9s} | {nilaiTugas:5d} | {nilaiUts:5d} | {nilaiUas:5d} | {nilaiAkhir:6.2f} |" .format(no=i, nama=item[0], nim=item[1], nilaiTugas=item[2], nilaiUts=item[3], nilaiUas=item[4], nilaiAkhir=item[5])) print("==================================================================")

Flowchart

![input end](https://github.com/yuliyanti12/tugaspraktikum4/blob/master/gambar/flaw%20cart.docx)

Input

![input end](https://github.com/yuliyanti12/tugaspraktikum4/blob/master/gambar/Praktikum04.png)