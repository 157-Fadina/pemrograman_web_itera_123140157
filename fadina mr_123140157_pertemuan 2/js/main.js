'use strict';

// Import logika dari file app.js
import { updateTime, fetchQuote, TodoApp } from './app.js';

// Menunggu semua elemen HTML dimuat
document.addEventListener('DOMContentLoaded', () => {

    // --- Eksekusi Widget 1: Jam Digital ---
    setInterval(updateTime, 1000);
    updateTime(); 

    // --- Eksekusi Widget 2: Quote of the Day ---
    fetchQuote();

    // --- Eksekusi Widget 3: Daftar Tugas (Diperbarui) ---
    
    // Ambil elemen DOM
    const todoListEl = document.getElementById('todo-list');
    const todoFormEl = document.getElementById('todo-form');
    // Ambil input baru
    const todoTitleEl = document.getElementById('todo-title');
    const todoDescEl = document.getElementById('todo-desc');
    const todoStartEl = document.getElementById('todo-start');
    const todoEndEl = document.getElementById('todo-end');


    // Pastikan semua elemen ada sebelum membuat instance
    if (todoListEl && todoFormEl && todoTitleEl && todoDescEl && todoStartEl && todoEndEl) {
        
        // Kirim semua elemen ke constructor TodoApp
        const myTodoApp = new TodoApp(
            todoListEl, 
            todoFormEl, 
            todoTitleEl, 
            todoDescEl, 
            todoStartEl, 
            todoEndEl
        );
        
        // Jalankan aplikasi
        myTodoApp.init();
    } else {
        console.error("Elemen To-Do list tidak lengkap!");
    }
    
});