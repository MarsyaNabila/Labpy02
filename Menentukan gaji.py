gaji = int(input("Masukkan gaji: ")) 
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T) ").strip().upper() == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T) ").strip().upper() == "Y"]

if gaji > 3000000:
    print("Gaji sudah di atas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")

    if punya_rumah:
        print("Wajib bayar pajak rumah")
    else:
        print("Tidak wajib bayar pajak rumah")
else:
    print("Gaji belum UMR")