'use strict';

// Fungsi updateTime dan fetchQuote tidak berubah (tetap di atas)
export const updateTime = () => {
    // ... (kode sama persis seperti sebelumnya)
    const clockElement = document.getElementById('clock');
    const dateElement = document.getElementById('date');
    if (!clockElement || !dateElement) return;
    const now = new Date();
    const timeString = now.toLocaleTimeString('id-ID', { hour12: false });
    const dateString = now.toLocaleDateString('id-ID', {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        year: 'numeric'
    });
    clockElement.textContent = timeString;
    dateElement.textContent = dateString;
};

export const fetchQuote = async () => {
    // ... (kode sama persis seperti sebelumnya)
    const quoteTextElement = document.getElementById('quote-text');
    const quoteAuthorElement = document.getElementById('quote-author');
    if (!quoteTextElement || !quoteAuthorElement) return;
    try {
        const response = await fetch('https://api.quotable.io/random');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        quoteTextElement.textContent = `"${data.content}"`;
        quoteAuthorElement.textContent = `— ${data.author}`;
    } catch (error) {
        console.error("Gagal mengambil quote:", error);
        quoteTextElement.textContent = "Gagal memuat kutipan. Coba refresh.";
    }
};

// ==========================================================
// Widget 3: Logika Daftar Tugas (Class Diperbarui)
// ==========================================================

export class TodoApp {
    // Constructor diperbarui untuk menerima input baru
    constructor(listEl, formEl, titleInput, descInput, startInput, endInput) {
        this.todoListElement = listEl;
        this.todoFormElement = formEl;
        // Input elements
        this.titleInput = titleInput;
        this.descInput = descInput;
        this.startInput = startInput;
        this.endInput = endInput;
        
        this.localStorageKey = 'myTodos';
        this.todos = this.loadFromStorage();
    }

    init() {
        this.todoFormElement.addEventListener('submit', (event) => {
            event.preventDefault(); 
            
            // Ambil data dari semua input
            const title = this.titleInput.value.trim();
            const description = this.descInput.value.trim();
            const startDate = this.startInput.value;
            const endDate = this.endInput.value;

            if (title !== "") {
                this.addTodo(title, description, startDate, endDate);
                // Reset form
                this.todoFormElement.reset();
            }
        });
        this.render();
    }

    // addTodo diperbarui
    addTodo(title, description, startDate, endDate) {
        const newTodo = {
            id: Date.now(),
            title: title, // sebelumnya 'text'
            description: description,
            startDate: startDate,
            endDate: endDate,
            completed: false
        };
        this.todos.push(newTodo);
        this.saveToStorage();
        this.render();
    }

    // render diperbarui untuk menampilkan data baru
    render() {
        this.todoListElement.innerHTML = "";

        if (this.todos.length === 0) {
            this.todoListElement.innerHTML = "<li>Belum ada tugas.</li>";
            return;
        }

        this.todos.forEach(todo => {
            const li = document.createElement('li');
            if (todo.completed) {
                li.classList.add('completed');
            }

            // [Helper Function] Format tanggal agar lebih rapi
            const formatDate = (dateString) => {
                if (!dateString) return "N/A";
                const date = new Date(dateString);
                return date.toLocaleDateString('id-ID', { day: '2-digit', month: 'short', year: 'numeric' });
            };

            // Template literal diperbarui untuk menampilkan semua data
            li.innerHTML = `
                <div style="padding-bottom: 10px;">
                    <strong class="task-title" style="font-size: 1.2em; cursor: pointer;">
                        ${todo.title}
                    </strong>
                    <br>
                    <small>
                        ${todo.description || '<i>Tidak ada deskripsi</i>'}
                    </small>
                    <br>
                    <small style="color: #333;">
                        [ ${formatDate(todo.startDate)} s.d. ${formatDate(todo.endDate)} ]
                    </small>
                </div>
                <div class="todo-actions">
                    <button class="edit-btn">✏️</button>
                    <button class="delete-btn">🗑️</button>
                </div>
                <hr>
            `;

            // Event listener dipindahkan ke elemen yang lebih spesifik
            li.querySelector('.edit-btn').addEventListener('click', () => {
                this.editTodo(todo.id);
            });

            li.querySelector('.delete-btn').addEventListener('click', () => {
                this.deleteTodo(todo.id);
            });

            // Judul di-klik untuk toggle complete
            li.querySelector('.task-title').addEventListener('click', () => {
                this.toggleComplete(todo.id);
            });

            this.todoListElement.appendChild(li);
        });
    }

    // editTodo diperbarui
    editTodo(id) {
        const todo = this.todos.find(t => t.id === id);
        
        // Gunakan prompt untuk setiap field
        const newTitle = prompt("Edit Judul:", todo.title);
        // Cek jika user menekan 'Cancel'
        if (newTitle === null) return; 
        
        const newDesc = prompt("Edit Deskripsi:", todo.description);
        const newStart = prompt("Edit Tgl Mulai (YYYY-MM-DD):", todo.startDate);
        const newEnd = prompt("Edit Tgl Selesai (YYYY-MM-DD):", todo.endDate);
        
        if (newTitle.trim() !== "") {
            todo.title = newTitle.trim();
            todo.description = newDesc ? newDesc.trim() : "";
            todo.startDate = newStart;
            todo.endDate = newEnd;
            
            this.saveToStorage();
            this.render();
        }
    }
    
    // Metode lain (toggleComplete, deleteTodo, saveToStorage, loadFromStorage)
    // tidak perlu diubah secara signifikan
    
    toggleComplete(id) {
        const todoToToggle = this.todos.find(todo => todo.id === id);
        todoToToggle.completed = !todoToToggle.completed;
        this.saveToStorage();
        this.render();
    }

    deleteTodo(id) {
        if (confirm("Apakah Anda yakin ingin menghapus tugas ini?")) {
            this.todos = this.todos.filter(todo => todo.id !== id);
            this.saveToStorage();
            this.render();
        }
    }
    
    saveToStorage() {
        localStorage.setItem(this.localStorageKey, JSON.stringify(this.todos));
    }

    loadFromStorage() {
        const todosString = localStorage.getItem(this.localStorageKey);
        return todosString ? JSON.parse(todosString) : [];
    }
}