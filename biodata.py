print("Selamat Datang di Program Input Biodata!")
print("========================================")
print("Siapkan Data-Data Berikut Agar Lebih Memudahkan Untuk Menginput Data: ")
biodata = ["1. Nama", "2. NIM", "3. Kelas", "4. Angkatan", "5. Tinggi Badan (satuan meter)", "6. Berat Badan (satuan kg)", "7. Tempat, Tanggal Lahir", "8. Alamat"]
for i in biodata:
    print(i)
print("=====================================================================")
def biodata():
    print("Mulai Menginput Biodata!")
    nama = str(input("Nama: "))
    nim = int(input("NIM: "))
    kelas = str(input("Kelas: "))
    angkatan = int(input("Angkatan: "))
    tinggi_badan = float(input("Tinggi Badan (satuan meter): "))
    berat_badan = float(input("Berat Badan (satuan kg): "))
    ttl = str(input("Tempat, Tanggal Lahir: "))
    Alamat = str(input("Alamat: "))
    print("=====================================================================")
    print("Apakah Ingin Menginput Biodata Lagi? ")
    x = int(input("Ketik '1' Jika Ingin Menginput Biodata Lagi dan Ketik Angka Yang Lainnya Untuk Berhenti: "))
    if x == 1:
        biodata()
    else:
        print("Terimakasih Telah Menggunakan Program Kami!")
biodata()
