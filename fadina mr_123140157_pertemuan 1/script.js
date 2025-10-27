document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskNameInput = document.getElementById('task-name');
    const courseNameInput = document.getElementById('course-name');
    const deadlineInput = document.getElementById('deadline');
    const taskList = document.getElementById('task-list');
    const incompleteCountEl = document.getElementById('incomplete-count');
    const filterStatus = document.getElementById('filter-status');
    const searchCourse = document.getElementById('search-course');
    
   let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    const saveTasks = () => {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    const renderTasks = () => {
        taskList.innerHTML = '';
        const statusValue = filterStatus.value;
        const searchValue = searchCourse.value.toLowerCase();

        const filteredTasks = tasks.filter(task => {
            const matchesStatus = (statusValue === 'all') ||
                                (statusValue === 'completed' && task.completed) ||
                                (statusValue === 'incomplete' && !task.completed);
            
            const matchesSearch = task.course.toLowerCase().includes(searchValue);

            return matchesStatus && matchesSearch;
        });

        if (filteredTasks.length === 0) {
             taskList.innerHTML = '<li class="no-tasks">🎉 Tidak ada tugas, waktunya bersantai!</li>';
        } else {
            filteredTasks.forEach(task => {
                const li = document.createElement('li');
                li.className = `task-item ${task.completed ? 'completed' : ''}`;
                li.setAttribute('data-id', task.id);

                li.innerHTML = `
                    <div class="task-info">
                        <span class="task-name">${task.name}</span>
                        <span class="task-details"><strong>Matkul:</strong> ${task.course} | <strong>Deadline:</strong> ${task.deadline}</span>
                    </div>
                    <div class="task-actions">
                        <button class="toggle-btn">${task.completed ? 'Batal' : 'Selesai'}</button>
                        <button class="delete-btn">Hapus</button>
                    </div>
                `;
                taskList.appendChild(li);
            });
        }
        
        updateIncompleteCount();
    };

    const updateIncompleteCount = () => {
        const incompleteTasks = tasks.filter(task => !task.completed).length;
        incompleteCountEl.textContent = incompleteTasks;
    };

    const addTask = (e) => {
        e.preventDefault(); 

        const taskName = taskNameInput.value.trim();
        const courseName = courseNameInput.value.trim();
        const deadline = deadlineInput.value;

        if (taskName === '' || courseName === '' || deadline === '') {
            alert('Mohon lengkapi semua field!');
            return;
        }
        
        const newTask = {
            id: Date.now(), 
            name: taskName,
            course: courseName,
            deadline: deadline,
            completed: false,
        };

        tasks.push(newTask);
        
        saveTasks();
        renderTasks();

        taskForm.reset();
    };

    const handleTaskListClick = (e) => {
        const target = e.target;
        const taskItem = target.closest('.task-item');
        if (!taskItem) return;

        const taskId = Number(taskItem.getAttribute('data-id'));

        if (target.classList.contains('toggle-btn')) {
            const taskIndex = tasks.findIndex(t => t.id === taskId);
            if (taskIndex > -1) {
                tasks[taskIndex].completed = !tasks[taskIndex].completed;
                saveTasks();
                renderTasks();
            }
        }

        if (target.classList.contains('delete-btn')) {
            if (confirm('Apakah Anda yakin ingin menghapus tugas ini?')) {
                tasks = tasks.filter(t => t.id !== taskId);
                saveTasks();
                renderTasks();
            }
        }
    };
    
    taskForm.addEventListener('submit', addTask);
    taskList.addEventListener('click', handleTaskListClick);
    filterStatus.addEventListener('change', renderTasks);
    searchCourse.addEventListener('input', renderTasks);

    renderTasks();
});