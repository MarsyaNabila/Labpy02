## Labpy02
## NAMA : MARSYA NABILA PUTRI
## NIM : 312410338
## KELAS : TI.24.A.4
## MATKUL : BAHASA PEMROGRAMAN 

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
fungsi print() adalah mencetak variable-variable pada program tersebut

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

# Menggunakan kondisi OR dengan menginputkan 3 bilangan 

```PYTHON

a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))
if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")

```

operator OR dalam python merubah beberapa kondisi dan mengembalikan true jika salah satu benar.

```PYTHON

a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

````

Program ini menginputkan sesuatu integer yang menggunakan variable a,b,c.

```PYTHON

if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")

````

jika (A) ditambah (B) haslnya (C) atau bahasa pemograman itu OR ,dan apabila (B) ditambah (C) hasilnya (A),dan (C) ditambah (A) maka hasilnya (B). maka output yang keluar adalah "benar"


# LATIHAN 3
# Pemesanan tiket bioskop

Kasus 1: Program Pemesanan Tiket Bioskop Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000, sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status member dari user, lalu menghitung total harga yang harus dibayar.

Petunjuk:
```
● Gunakan if else dan operator ternary.
```

```PYTHON
harga_reguler = 50000
harga_vip = 100000

tipe_tiket = (input("Masukkan tipe tiket (reguler/VIP): "))
status_member = (input("Apakah Anda memiliki kartu member? (ya/tidak): "))

 Menghitung total harga
if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
    total_harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

 Menghitung diskon jika pengguna memiliki kartu member


if status_member == "ya":
        total_harga *= 0.8  # Diskon 20%
    
        print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
elif status_member == "tidak":
            total_harga
            print(f"total harga yang harua dibayar: Rp{total_harga:.2f}")
else:
    print("Harga tidak dapat dihitung.")

````

Program ini akan menentukan harga pesanan tiket bioskop, Yang reguler/Vip, dan jika Vip harga 100.000, dan jika reguler 80.0000, dan jika memiliki kartu member pelanggan tersebut akan mendapatkan diskon 20%

```PYTHON

harga_reguler = 50000
harga_vip = 100000

````

variable ini menentukan harga tiket bioskop

```PYTHON

tipe_tiket = (input("Masukkan tipe tiket (reguler/VIP): "))
status_member = (input("Apakah Anda memiliki kartu member? (ya/tidak): "))

````

memasukan inputan sesuai Output Program (Reguler/Vip) di variable (Tipe_Tiket), dan Memasukan inputan yang output tersebut Bertanya memiliki kartu member atau tidak.

```PYTHON

if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
    total_harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

````

Jika tipe tiket reguler total harga proses ke Harga reguler, dan jika tiket vip Total harga proses keharga vip

dan jika Selain memasukan inputan reguler/vip Output yang keluar "Tipe tiket tidak valid" dan berproses ke fungsi exit() yang artinya program dihentikan.

```PYTHON

if status_member == "ya":
        total_harga *= 0.8  # Diskon 20%
    
        print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
elif status_member == "tidak":
            total_harga
            print(f"total harga yang harua dibayar: Rp{total_harga:.2f}")
else:
    print("Harga tidak dapat dihitung.")

```

desision ini menentukan mempunyai kartu member atau tidak, Jika Inputan status member menjawab "ya", maka total harga akan di kalikan dengan operator * 0,8 yang disebut diskon 20%

dan jika inputan status member "tidak", maka total harga normal

jika menginputkan selain (ya/tidak) output yang keluar "Harga tidak dapat dihitung"

Dan ini hasil program tersebut:

![WhatsApp Image 2024-10-27 at 09 55 37_54ccffa2](https://github.com/user-attachments/assets/a91c2556-6b95-48cc-b232-10d9510358cf)

Eksekusi dari program tersebut:

![WhatsApp Image 2024-10-27 at 10 09 33_23097a02](https://github.com/user-attachments/assets/f793271a-4da4-4ab9-ae09-341f30641d00)

Dan flowchartnya:

![flowchart baru](https://github.com/user-attachments/assets/a9813385-5db2-4939-b591-8c18d9ca99a4)


# Kalkulator sederhana 
# Kasus 2: Program Kalkulator Sederhana

Buat program kalkulator yang menerima dua angka dan satu operator aritmatika dari pengguna (penjumlahan, pengurangan, perkalian, atau pembagian). Program akan menghitung hasil sesuai dengan operator yang dipilih.

# Petunjuk: 

```

● Gunakan if elif else untuk menentukan operasi aritmatika.

angka1 = float(input("Masukkan angka pertama: "))

```

operator = input("Masukkan operator (+, -, *, /): ") angka2 = float(input("Masukkan angka kedua: "))

# Menghitung hasil berdasarkan operator

```PYTHON

if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print(f"Hasil pengurangan: {hasil}")
elif operator == '*':
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {hasil}")
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")

else:
    print("Error: Operator tidak valid. Silakan gunakan +, -, *, atau /.")

````

Program kalkulator sederhana dalam Python adalah proyek yang baik untuk pemula dan programmer tingkat lanjut. Program ini memungkinkan pengguna untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.

```PYTHON

angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

````

fungsi yang digunakan dalam inputan ini menggunakan float mengubah nilai menjadi angka floating point, yaitu angka desimal atau pecahan, dan variable operator yang menginputkan suatu operator fungsi berupa (+, -, *, /) yang artinya pertambahan, perkurang, perkali, pembagian.

```PYTHON

if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")

````

Jika operator (+), maka hasil tersbur inputan variable angka1 ditambahkan angka2, dan Output akan mengeluarkan hasil program tersebut, Hingga seterusnya dengan (*) perkalian, dan (-) perkurangan

```PYTHON

elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")

````

Jika oprator (/), maka Inputan Variable angka1 dibagi angka2, dan dicetak semestinya, untuk desision (angka2 !=0:) tidak diperkenankan oleh program, karna output yang keluar "Error: Pembagian dengan nol tidak diperbolehkan"

```PYTHON

else:
    print("Error: Operator tidak valid. Silakan gunakan +, -, *, atau /.")

````

saya memasukan desision else ini Karna jika menjawab selain fungsi operator ini Output yang keluar "Error: Operator tidak valid. Silakan gunakan +, -, *, atau /."

dan ini hasil program tersebut:

![WhatsApp Image 2024-10-27 at 11 16 35_7167fc7d](https://github.com/user-attachments/assets/047458d6-be05-4f9b-8b06-0f1f31c53397)

Eksekusi program tersebut:

<img width="960" alt="Screenshot 2024-10-27 111452" src="https://github.com/user-attachments/assets/6220640d-7fec-4e89-80aa-c6072a90548d">


Dan flowchartnya:

![Screenshot 2024-10-27 153830](https://github.com/user-attachments/assets/3d99b859-6ac9-4b99-b360-b53c130d5248)













































  



















