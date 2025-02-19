document.addEventListener('DOMContentLoaded', () => {
  const todoItems = document.querySelectorAll('.todo-item');
  const columns = document.querySelectorAll('.todo-column');
  const addTodoInputs = document.querySelectorAll('.add-todo');
  
  let draggedItem = null;

  // Setup drag and drop for existing items
  todoItems.forEach(item => {
    setupDragAndDrop(item);
  });

  function setupDragAndDrop(item) {
    item.addEventListener('dragstart', (e) => {
      draggedItem = item;
      setTimeout(() => {
        item.classList.add('dragging');
      }, 0);
    });

    item.addEventListener('dragend', () => {
      draggedItem.classList.remove('dragging');
      draggedItem = null;
    });
  }

  // Column drop zones
  columns.forEach(column => {
    column.addEventListener('dragover', (e) => {
      e.preventDefault();
      column.classList.add('droppable-hover');
    });

    column.addEventListener('dragleave', () => {
      column.classList.remove('droppable-hover');
    });

    column.addEventListener('drop', (e) => {
      e.preventDefault();
      column.classList.remove('droppable-hover');
      const itemsContainer = column.querySelector('.items-container');
      if (draggedItem) {
        itemsContainer.appendChild(draggedItem);
      }
    });
  });

  // Add new todo items
  addTodoInputs.forEach(input => {
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && input.value.trim() !== '') {
        const newTodo = document.createElement('div');
        newTodo.className = 'todo-item';
        newTodo.draggable = true;
        newTodo.textContent = input.value.trim();
        
        const itemsContainer = input.previousElementSibling;
        itemsContainer.appendChild(newTodo);
        
        setupDragAndDrop(newTodo);
        input.value = '';
      }
    });
  });
});