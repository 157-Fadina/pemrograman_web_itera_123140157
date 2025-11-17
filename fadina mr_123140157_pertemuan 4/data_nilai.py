data_mahasiswa = [
    {
        "nama": "Asep Supriatna",
        "NIM": "120140007",
        "nilai_uts": 85,
        "nilai_uas": 90,
        "nilai_tugas": 80,
    },
    {
        "nama": "Theo Hartanto",
        "NIM": "121140180",
        "nilai_uts": 65,
        "nilai_uas": 75,
        "nilai_tugas": 70,
    },
    {
        "nama": "Citra Lestari",
        "NIM": "122140123",
        "nilai_uts": 90,
        "nilai_uas": 85,
        "nilai_tugas": 95,
    },
    {
        "nama": "Dian Pratama",
        "NIM": "123140156",
        "nilai_uts": 55,
        "nilai_uas": 60,
        "nilai_tugas": 50,
    },
    {
        "nama": "Eko Widodo",
        "NIM": "124140199",
        "nilai_uts": 75,
        "nilai_uas": 65,
        "nilai_tugas": 70,
    },

    {
        "nama": "Mustika Tarigan",
        "NIM": "125140157",
        "nilai_uts": 88,
        "nilai_uas": 92,
        "nilai_tugas": 85,

    },
]

def hitung_nilai_akhir(uts, uas, tugas):
    """Menghitung nilai akhir berdasarkan bobot."""
    nilai_akhir = (0.3 * uts) + (0.4 * uas) + (0.3 * tugas)
    return round(nilai_akhir, 2)

def tentukan_grade(nilai_akhir):
    """Menentukan grade berdasarkan nilai akhir."""
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"
    
def hitung_rata_rata_kelas(data):
    """Menghitung rata-rata nilai akhir seluruh mahasiswa."""
    if not data:
        return 0
    total_nilai_akhir = 0
    for mhs in data:
        na = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        total_nilai_akhir += na
    rata_rata = total_nilai_akhir / len(data)
    return round(rata_rata, 2)

def tampilkan_data(data):
    """Menampilkan data mahasiswa dalam format tabel."""
    print("\n" + "="*80)
    print(f"{'| NIM':<10} | {'Nama Mahasiswa':<20} | {'UTS':<5} | {'UAS':<5} | {'Tugas':<7} | {'Nilai Akhir':<12} | {'Grade':<5} |")
    print("="*80)

    if not data:
        print("|                             *** Tidak ada data mahasiswa *** |")
    else:
        for mhs in data:
            nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
            grade = tentukan_grade(nilai_akhir)
            
            print(f"| {mhs['NIM']:<8} | {mhs['nama']:<20} | {mhs['nilai_uts']:<5} | {mhs['nilai_uas']:<5} | {mhs['nilai_tugas']:<7} | {nilai_akhir:<12} | {grade:<5} |")
        
    print("="*80)

    if data:
        rata_rata = hitung_rata_rata_kelas(data)
        print(f"** Rata-rata Nilai Akhir Kelas: {rata_rata}")

def cari_min_max(data, tipe='tertinggi'):
    """Mencari mahasiswa dengan nilai akhir tertinggi atau terendah."""
    if not data:
        print("Data mahasiswa kosong.")
        return

    mahasiswa_dengan_na = []
    for mhs in data:
        na = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        mahasiswa_dengan_na.append((mhs, na))

    if tipe == 'tertinggi':
        hasil = max(mahasiswa_dengan_na, key=lambda x: x[1])
        label = "Tertinggi"
    else:
        hasil = min(mahasiswa_dengan_na, key=lambda x: x[1])
        label = "Terendah"
    
    mhs_terpilih = hasil[0]
    nilai = hasil[1]
    grade = tentukan_grade(nilai)

    print(f"\n✨ Mahasiswa dengan Nilai Akhir {label}:")
    print(f"  Nama: {mhs_terpilih['nama']}")
    print(f"  NIM: {mhs_terpilih['NIM']}")
    print(f"  Nilai Akhir: {nilai}")
    print(f"  Grade: {grade}")


def input_mahasiswa_baru(data):
    """Mengambil input data mahasiswa baru dari user."""
    print("\n➕ Masukkan Data Mahasiswa Baru:")
    
    nama = input("  Nama Mahasiswa: ").strip()
    nim = input("  NIM: ").strip()
    
    while True:
        try:
            uts = int(input("  Nilai UTS (0-100): "))
            uas = int(input("  Nilai UAS (0-100): "))
            tugas = int(input("  Nilai Tugas (0-100): "))
            if all(0 <= n <= 100 for n in [uts, uas, tugas]):
                break
            else:
                print("⚠️ Nilai harus berada dalam rentang 0-100. Coba lagi.")
        except ValueError:
            print("⚠️ Input nilai tidak valid. Harap masukkan angka.")

    data_baru = {
        "nama": nama,
        "NIM": nim,
        "nilai_uts": uts,
        "nilai_uas": uas,
        "nilai_tugas": tugas,
    }
    data.append(data_baru)
    print(f"\n✅ Data {nama} berhasil ditambahkan!")

def filter_berdasarkan_grade(data):
    """Memfilter dan menampilkan mahasiswa berdasarkan grade."""
    target_grade = input("  Masukkan Grade yang ingin difilter (A/B/C/D/E): ").upper().strip()
    
    if target_grade not in ('A', 'B', 'C', 'D', 'E'):
        print("⚠️ Grade tidak valid. Harap masukkan A, B, C, D, atau E.")
        return

    hasil_filter = []
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        if grade == target_grade:
            hasil_filter.append(mhs)
    
    print(f"\n🔬 Hasil Filter Mahasiswa Grade {target_grade}:")
    tampilkan_data(hasil_filter)

def main():
    """Fungsi utama untuk menjalankan program."""
    global data_mahasiswa

    while True:
        print("\n" + "="*40)
        print("🎓 PROGRAM PENGELOLAAN DATA NILAI MAHASISWA")
        print("="*40)
        print("1. Tampilkan Semua Data Nilai")
        print("2. Tambah Data Mahasiswa Baru")
        print("3. Cari Nilai Tertinggi")
        print("4. Cari Nilai Terendah")
        print("5. Filter Berdasarkan Grade")
        print("6. Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tampilkan_data(data_mahasiswa)
        elif pilihan == '2':
            input_mahasiswa_baru(data_mahasiswa)
        elif pilihan == '3':
            cari_min_max(data_mahasiswa, tipe='tertinggi')
        elif pilihan == '4':
            cari_min_max(data_mahasiswa, tipe='terendah')
        elif pilihan == '5':
            filter_berdasarkan_grade(data_mahasiswa)
        elif pilihan == '6':
            print("\nTerima kasih! Program selesai. 👋")
            break
        else:
            print("\n❌ Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()