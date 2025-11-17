# 📚 Sistem Manajemen Perpustakaan Sederhana (OOP Python)

1. Deskripsi Program dan Fitur Utama
    Program ini adalah implementasi sistem manajemen perpustakaan sederhana yang dibangun menggunakan bahasa pemrograman Python dengan fokus pada konsep Object-Oriented Programming (OOP).

    * Konsep OOP yang Diterapkan:
        - Abstract Class & Inheritance, yaitu kelas dasar LibraryItem adalah kelas abstrak (ABC) yang diwarisi oleh Book dan Magazine.
        
        - Encapsulation, yaitu data penting seperti, <i> koleksi item __collection dan atribut item _title </i> dilindungi menggunakan access modifier (private/protected) dan diakses melalui getter.

        - Property Decorator digunakan pada atribut isbn di kelas Book untuk mengontrol akses dan memvalidasi input data.

        - Polymorphism adalah metode <b> get_details() </b> diimplementasikan secara berbeda pada setiap subclass Book dan Magazine, yang memungkinkan pemanggilan tunggal di kelas Library untuk menampilkan detail yang tepat.

    * Fitur-Fitur Program:
        - Menambah Item dengan menggunakan fungsi <b> add_new_item_interactively() </b> untuk menambahkan objek Book atau Magazine baru ke dalam koleksi perpustakaan.

        - Menampilkan Daftar, dengan method <b> display_items() </b> mencetak seluruh koleksi yang tersedia, menampilkan detail spesifik item.

        - Mencari Item, dengan method <b> search_item() </b> memungkinkan pencarian item berdasarkan judul atau ID unik.

2. Screenshot Hasil Running Program 
    Berikut adalah contoh hasil running program di terminal, yang mendemonstrasikan penambahan item secara interaktif, perubahan data menggunakan property setter, dan pencarian.

    * Penjelasan Output:

        - Program diawali dengan menambahkan item non-interaktif (The Hobbit).
        - Program meminta input untuk Item 1 (misalnya, Majalah) dan Item 2 (misalnya, Buku).
        - Output menunjukkan demonstrasi property setter (ISBN untuk 'Filsafat Teras' berhasil diubah).
        - Daftar koleksi lengkap (termasuk item yang baru ditambahkan) dicetak.
        - Fungsi pencarian memvalidasi item yang dicari (Atomic Habits).

3. Diagram Kelas (Class Diagram)
    Diagram berikut memvisualisasikan struktur kelas dan hubungan di antara mereka, menunjukkan bagaimana konsep Inheritance dan Encapsulation diterapkan.

    [foto]

    Detail Hubungan:
    * LibraryItem (Abstract): Memiliki atribut protected (#) dan operasi abstrak ({abstract}).
    * Book dan Magazine: Mewarisi (<|--) dari LibraryItem.
    * Library: Memiliki hubungan komposisi (1..*) dengan LibraryItem (melalui koleksi __collection), yang berarti Library mengelola banyak (*) objek LibraryItem.