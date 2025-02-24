document.querySelector('.search').addEventListener('input', function(e) {
    const searchText = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('.table tbody tr');
    
    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(searchText) ? '' : 'none';
    });
  });
  
  document.querySelectorAll('.table th').forEach(header => {
    header.addEventListener('click', function() {
      const index = Array.from(this.parentNode.children).indexOf(this);
      const rows = Array.from(document.querySelectorAll('.table tbody tr'));
      const isNumeric = index === 0;
      
      rows.sort((a, b) => {
        const aVal = a.children[index].textContent;
        const bVal = b.children[index].textContent;
        
        if (isNumeric) {
          return parseInt(aVal) - parseInt(bVal);
        }
        return aVal.localeCompare(bVal);
      });
      
      const tbody = document.querySelector('.table tbody');
      rows.forEach(row => tbody.appendChild(row));
    });
  });
  
  document.querySelectorAll('.btn-danger').forEach(btn => {
    btn.addEventListener('click', function() {
      if (confirm('Вы уверены, что хотите удалить эту запись?')) {
        const row = this.closest('tr');
        row.style.opacity = '0';
        setTimeout(() => row.remove(), 300);
      }
    });
  });
  
  document.querySelectorAll('.btn-success').forEach(btn => {
    btn.addEventListener('click', function() {
      const row = this.closest('tr');
      const id = row.querySelector('td').textContent;
      alert(`Редактирование записи #${id}`);
    });
  });
  
  document.querySelectorAll('.filter-select').forEach(select => {
    select.addEventListener('change', function() {
      console.log('Применен фильтр:', this.value);
    });
  });
  
  document.querySelectorAll('.page-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      if (!this.classList.contains('active')) {
        document.querySelector('.page-btn.active')?.classList.remove('active');
        this.classList.add('active');
      }
    });
  });
