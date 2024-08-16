function toggleTask(taskId) {
    window.location.href = `/toggle/${taskId}`;
}

function editTask(taskId) {
    const listItem = document.querySelectorAll('#task-list li')[taskId];
    const taskContent = listItem.querySelector('.task-content');
    const currentText = taskContent.textContent;

    const input = document.createElement('input');
    input.type = 'text';
    input.value = currentText;
    input.style.width = '100%';

    taskContent.textContent = '';
    taskContent.appendChild(input);
    input.focus();

    input.addEventListener('blur', function() {
        updateTask(taskId, this.value);
    });

    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            updateTask(taskId, this.value);
        }
    });
}

function updateTask(taskId, newContent) {
    fetch(`/update/${taskId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `content=${encodeURIComponent(newContent)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.reload();
        }
    });
}

function deleteTask(taskId) {
    if (confirm('Are you sure you want to delete this task?')) {
        window.location.href = `/delete/${taskId}`;
    }
}