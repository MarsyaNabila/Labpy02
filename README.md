### Labpy02
### Nama : MARSYA NABILA PUTRI
### Kelas : TI.24.A.4
### Matkul : BAHASA PEMROGRAMAN 

# LATIHAN 1
# Program Perhitungan Nilai Akhir Siswa
## Deskripsi
Program ini adalah aplikasi sederhana untuk menghitung nilai akhir seorang siswa berdasarkan nilai UTS (Ujian Tengah Semester), UAS (Ujian Akhir Semester), dan nilai Tugas. Program ini juga menentukan apakah siswa tersebut lulus atau tidak, serta memberikan nilai huruf berdasarkan nilai akhir.

## Fitur

- Memasukkan nama siswa.
- Memasukkan nilai UTS, UAS, dan Tugas.
- Menghitung nilai akhir berdasarkan bobot yang telah ditentukan.
- Menentukan keterangan lulus atau tidak lulus.
- Memberikan nilai huruf sesuai dengan nilai akhir.

## Detail Kode

1. **Pengambilan Input**:
   - Program meminta pengguna untuk memasukkan nama siswa dan nilai-nilai (UTS, UAS, dan Tugas).
   ```python
   nama = input("Masukkan nama:")
   uts = input("Masukkan nilai UTS:")
   uas = input("Masukkan nilai UAS:")
   tugas = input("Masukkan nilai Tugas:")
Perhitungan Nilai Akhir:

Nilai akhir dihitung dengan rumus:
nilai akhir

```
nilai akhir=(nilai tugas×0.2)+(nilai UTS×0.4)+(nilai UAS×0.4)
```
Nilai tugas memiliki bobot 20%, sedangkan UTS dan UAS masing-masing memiliki bobot 40%.
```python
Copy code
akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
Penentuan Keterangan Lulus/Tidak Lulus:
```
Program menentukan apakah siswa lulus jika nilai akhir lebih dari 60.0.
```python
Copy code
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
Penentuan Nilai Huruf:
```
Nilai huruf ditentukan berdasarkan nilai akhir:
A: lebih dari 80
B: lebih dari 70
C: lebih dari 50
D: lebih dari 40
E: 40 atau kurang
```python
Copy code
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"
Output Hasil:
```
Program mencetak nama siswa, nilai UTS, UAS, Tugas, nilai akhir, nilai huruf, dan keterangan lulus atau tidak.
```python
Copy code
print("\nNama :",nama)
print("Nilai UTS :",uts)
print("Nilai UAS :",uas)
print("Nilai Tugas :",tugas)
print("Nilai Akhir :",akhir)
print("\nNilai Huruf :",huruf)
print("Keterangan :",keterangan)
```
Cara Menjalankan
Pastikan Python telah terinstal di komputer Anda.
Salin kode ke dalam file Python (misalnya, nilai_siswa.py).
Jalankan file tersebut menggunakan terminal atau command prompt.
Gunakan perintah cd untuk berpindah ke direktori.
Ketikkan perintah berikut untuk menjalankan file:
Setelah Anda menjalankan perintah tersebut, program akan dieksekusi, dan Anda akan melihat output di terminal atau command prompt.

## screenshot visual studio code

<img width="595" alt="Screenshot 2024-10-25 174158" src="https://github.com/user-attachments/assets/c27eaf3c-c54f-4de2-948d-8a58c84f41ba">

## Penjelasan

- Tugas UTS, dan UAS dimasukkan oleh pengguna sebagai input dengan float.
- Nilai akhir dihitung menggunakan bobot tertentu (20% tugas, 40% UTS, 40% UAS).
- Berdasarkan nilai akhir, program menentukan nilai huruf dan keterangan kelulusan.

# LATIHAN 2

# Program Pengecekan Gaji, Status Keluarga, dan Kepemilikan Rumah

### Deskripsi
Program ini menerima input gaji, status keluarga (sudah berkeluarga atau belum), dan status kepemilikan rumah dari pengguna, kemudian melakukan beberapa pengecekan sebagai berikut:
1. Apakah gaji di atas UMR (Upah Minimum Regional).
2. Jika gaji di atas UMR, program akan mengecek apakah pengguna sudah berkeluarga untuk menentukan kewajiban mengikuti asuransi dan menabung.
3. Program juga mengecek apakah pengguna memiliki rumah untuk menentukan kewajiban membayar pajak rumah.

## Cara Kerja Program
1. Program meminta input dari pengguna untuk gaji, status berkeluarga, dan status kepemilikan rumah.
2. Jika gaji lebih dari 3.000.000, program akan mencetak "Gaji sudah di atas UMR". Jika tidak, akan mencetak "Gaji belum UMR".
3. Jika pengguna sudah berkeluarga, program akan mencetak "Wajib ikutan asuransi dan menabung untuk pensiun",namun jika belum berkeluarga, akan mencetak "Tidak perlu ikutan asuransi".
4. Jika pengguna memiliki rumah, program akan mencetak "Wajib bayar pajak rumah". Jika tidak memiliki rumah, akan mencetak "Tidak wajib bayar pajak rumah".

## Struktur Program 
- Input:
   - Gaji (int)
   - Status berkeluarga (Y/T)
   - Status kepemilikan rumah (Y/T)
- Output:
  
   - Apakah gaji sudah di atas UMR atau belum
   - Kewajiban mengikuti asuransi jika sudah berkeluarga
   - Kewajiban membayar pajak rumah jika punya rumah

## Contoh Penggunaan

# Gaji di atas UMR

```
Masukan gaji: 500000000
Sudah berkeluarga? (Y/T): Y
Punya rumah? (Y/T): Y

Gaji sudah diatas UMR
Wajib ikutin asuransi dan menabung untuk pensiun
Tidak wajib bayar pajak rumah

```

# Berikut hasil screenshot visual studio code

<img width="960" alt="Screenshot 2024-10-25 181619" src="https://github.com/user-attachments/assets/a04bcb90-b269-4a00-a748-60c06fae7baa">

# gaji dibawah UMR

```

Masukan gaji: 3000000
Sudah berkeluarga? (Y/T): Y
Punya rumah? (Y/T): Y

Gaji belum diatas UMR
Wajib ikutin asuransi dan menabung untuk pensiun
Tidak wajib bayar pajak rumah

```

# Berikut Hasil Screenshot Visual Code

<img width="960" alt="Screenshot 2024-10-25 182420" src="https://github.com/user-attachments/assets/3262775b-27a0-47c4-bed4-8a682e0fca7e">

# Penjelasan

- Pengecekan berkaluarga dan punya rumah: Variabel berkeluarga dan punya_rumah dicek dengan perbandingan input terhadap "Y menggunakan input().strip() == "Y", yang memastikan bahwa input diubah menjadi huruf kapital dan mengabaikan spasi yang tidak perlu.
-  Program ini menggunakan if-else untuk menentukan pesan yang akan ditampilkan berdasarkan kondisi gaji status keluarga, dan status kepemilikan rumah.
  



















