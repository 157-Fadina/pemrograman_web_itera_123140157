from abc import ABC, abstractmethod
import uuid

class LibraryItem(ABC):
    """
    Abstract Base Class untuk semua item di perpustakaan.
    Menerapkan konsep class dan abstract method.
    """
    def __init__(self, title, year):
        self._title = title
        self._year = year
        self._item_id = str(uuid.uuid4())[:8] # ID unik singkat

    @abstractmethod
    def get_details(self):
        """Method abstract: Harus diimplementasikan oleh subclass."""
        pass

    def get_id(self):
        """Mengembalikan ID unik item."""
        return self._item_id

    def get_title(self):
        """Mengembalikan judul item."""
        return self._title

    def __str__(self):
        """Representasi string dari LibraryItem."""
        return f"ID: {self._item_id} | Judul: {self._title} ({self._year})"

class Book(LibraryItem):
    """
    Subclass dari LibraryItem untuk merepresentasikan buku.
    Mewarisi dari LibraryItem.
    """
    def __init__(self, title, year, author, isbn):
        super().__init__(title, year)
        self._author = author
        self._isbn = isbn

    @property
    def isbn(self):
        """Getter untuk ISBN."""
        return self._isbn

    @isbn.setter
    def isbn(self, new_isbn):
        """Setter untuk ISBN dengan validasi sederhana."""
        if len(new_isbn) == 13 and new_isbn.isdigit():
            self._isbn = new_isbn
            print(f"ISBN untuk '{self._title}' berhasil diubah.")
        else:
            print("Error: ISBN harus 13 digit numerik.")

    # Implementasi method abstract (Polymorphism)
    def get_details(self):
        """Mengembalikan detail lengkap buku."""
        return f"Buku: '{self._title}' oleh {self._author} ({self._year}), ISBN: {self._isbn}"

class Magazine(LibraryItem):
    """
    Subclass dari LibraryItem untuk merepresentasikan majalah.
    Mewarisi dari LibraryItem.
    """
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self._issue_number = issue_number

    def get_details(self):
        """Mengembalikan detail lengkap majalah."""
        return f"Majalah: '{self._title}' Edisi #{self._issue_number} ({self._year})"
    
    def show_issue(self):
        """Menampilkan nomor edisi majalah."""
        return f"Ini adalah edisi ke-{self._issue_number} dari {self._title}."

# --- Konsep Encapsulation dan Class Management ---

class Library:
    """
    Kelas untuk mengelola koleksi item perpustakaan.
    Menerapkan encapsulation untuk koleksi item.
    """
    def __init__(self):
        self.__collection = []

    # Metode untuk menambahkan item
    def add_item(self, item):
        """Menambahkan item (Book/Magazine) ke koleksi."""
        if isinstance(item, LibraryItem):
            self.__collection.append(item)
            print(f"✅ Item '{item.get_title()}' berhasil ditambahkan (ID: {item.get_id()}).")
        else:
            print("❌ Error: Objek yang ditambahkan harus merupakan turunan dari LibraryItem.")

    # Metode untuk menampilkan daftar item (Polymorphism)
    def display_items(self):
        """Menampilkan semua item yang ada di perpustakaan."""
        if not self.__collection:
            print("\n📚 Perpustakaan masih kosong.")
            return

        print("\n--- DAFTAR KOLEKSI PERPUSTAKAAN ---")
        for item in self.__collection:
            # Penggunaan Polymorphism: Memanggil method get_details()

            print(f"- {item.get_details()} | {item}")
        print("-----------------------------------")

    # Metode untuk mencari item
    def search_item(self, query):
        """Mencari item berdasarkan judul atau ID."""
        results = []
        for item in self.__collection:
            # Mencari berdasarkan ID atau Judul 
            if query.lower() in item.get_id().lower() or \
               query.lower() in item.get_title().lower():
                results.append(item)
        
        if results:
            print(f"\n🔍 Ditemukan {len(results)} hasil untuk '{query}':")
            for item in results:
                print(f"- {item.get_details()}")
        else:
            print(f"\n❌ Tidak ditemukan item dengan judul/ID '{query}'.")


def add_new_item_interactively(library_object):
    """Meminta input dari user untuk membuat dan menambahkan Buku atau Majalah."""
    
    print("\n--- TAMBAH ITEM BARU ---")
    
    # 1. Pilih Tipe Item
    while True:
        item_type = input("Pilih tipe item (1: Buku, 2: Majalah): ").strip()
        if item_type in ['1', '2']:
            break
        print("Pilihan tidak valid. Silakan masukkan '1' atau '2'.")

    # 2. Input Data Umum
    title = input("Masukkan Judul: ").strip()
    year = input("Masukkan Tahun Terbit: ").strip()
    
    # Validasi input tahun sederhana
    while not year.isdigit() or len(year) != 4:
        print("Tahun harus 4 digit angka.")
        year = input("Masukkan Tahun Terbit: ").strip()
        
    # 3. Input Data Spesifik dan Membuat Objek
    if item_type == '1': # Buku
        author = input("Masukkan Nama Penulis: ").strip()
        isbn = input("Masukkan ISBN (13 digit): ").strip()
        
        # Sederhana: membuat objek tanpa validasi ISBN ketat di sini
        new_item = Book(title, int(year), author, isbn)
        
    elif item_type == '2': # Majalah
        issue_number = input("Masukkan Nomor Edisi: ").strip()
        
        # Validasi input edisi sederhana
        while not issue_number.isdigit():
            print("Nomor Edisi harus angka.")
            issue_number = input("Masukkan Nomor Edisi: ").strip()
            
        new_item = Magazine(title, int(year), int(issue_number))

    # 4. Tambahkan ke Library
    library_object.add_item(new_item)

# --- Demonstrasi Penggunaan (Diperbarui) ---

print("\n--- DEMO SISTEM MANAJEMEN PERPUSTAKAAN (Interaktif) ---")

library = Library()
library.add_item(Book("Filsafat Teras", 2020, "Henry Manampiring", "9786020647895"))
library.add_item(Magazine("National Geographic", 2025, 451))

library.display_items()

book_awal = Book("The Hobbit", 1937, "J.R.R. Tolkien", "9780261102217")
library.add_item(book_awal)

add_new_item_interactively(library)

add_new_item_interactively(library)

library.display_items()

search_query = input("\nMasukkan Judul/ID untuk dicari: ").strip()
library.search_item(search_query)