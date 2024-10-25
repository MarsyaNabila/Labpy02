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
Jalankan file tersebut menggunakan

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







