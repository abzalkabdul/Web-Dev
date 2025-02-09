let display = document.getElementById('display');
let add = document.getElementById('add');
let container = document.getElementById('container');

add.addEventListener('click', () => {
    let newTask = display.value.trim();
    if (!newTask) return alert('Please write task');

    let taskDiv = document.createElement('div');
    taskDiv.className = 'task-item';

    let checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'task-checkbox';
    
    let taskText = document.createElement('span');
    taskText.textContent = newTask;
    taskText.className = 'task-text';
    
    let deleteAdd = document.createElement('button');
    deleteAdd.textContent = '🗑';
    deleteAdd.className = 'delete-add';

    checkbox.addEventListener('change', () => {
        taskText.classList.toggle('completed', checkbox.checked);
    });

    deleteAdd.addEventListener('click', () => taskDiv.remove());

    taskDiv.append(checkbox, taskText, deleteAdd);
    container.appendChild(taskDiv);
    display.value = '';
});
